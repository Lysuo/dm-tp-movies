import os
import json
import subprocess
import time

from dmapp.models import MovieEntry, ParamEntry

import sys    # sys.setdefaultencoding is cancelled by site.py
reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')


def load():
  s = ParamEntry.objects.get(mName='sessionTP')
  sessionTP = s.mValue
  print "session TP : " + sessionTP
  return sessionTP


def getResponse(inCmd):
  proc = subprocess.Popen([inCmd], stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  return out

def getMoviesJSON(sessionTP):
  cmd = "curl -X POST --data 'type=202&session="+sessionTP+"&club=TRANS&maxRows=1000' 'http://10.1.0.146/TPMCOREWeb/Vod' > dmapp/movies.json 2> /dev/null"
  o = getResponse(cmd)
#  = json.loads(o)


def parseJson():
  with open('dmapp/movies.json') as data_file:    
    data = json.load(data_file)

  IDexisting = MovieEntry.objects.all().values_list('mID', flat=True)
  logE = ""
  nbE = 0
  date = time.strftime("%c")

  nbCat = len(data['ResponseVO']['categories'])
  i=0
  sumM=0
  header = "TYPE;CAT;NB_CAT;ID;NAME;ORIGINAL NAME;COUNTRY;YEAR;GENRE;VOTES;DESCRP;DIRECTOR;ACTORS;IMG;IMDB?;I_NAME;I_YEAR;I_DATE;I_DIRECTOR;I_ACTORS;I_PLOT;I_COUNTRY;I_LANGUAGE;I_GENRE;I_RATING;I_VOTES;I_AWARDS;I_IMG;FORMAT1;FORMAT2;FORMAT3;FORMAT4;FORMAT5"

#  print header
  IDsL = []

  while i<nbCat:
    catName = data['ResponseVO']['categories'][i]['CategoryVO']['categoryName']
    catNbMovies = len(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'])
    sumM += catNbMovies

    j=0
    while j<catNbMovies:
      movieID = str(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['vodId'])

      if movieID not in IDexisting:
        IDsL.append(movieID)
        IDexisting = MovieEntry.objects.all().values_list('mID', flat=True)

        movieGenre = data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['genre']
        movieName = data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['name']
        movieOName = data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['originalName']
        movieCountry = data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['country']
        movieYear = int(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['year'])
        movieDescription = str(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['description'])
        movieDirector = str(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['director'])
        movieActors = str(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['actors'])
        movieVotes = int(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['totalVotes'])
        movieIMG = data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['images']['url3X3']
        movieNbFormats = len(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['formats'])

        k=0
        formats = ["", "", "", "", "", "", "", ""]
        while k<movieNbFormats:

          formats[k] += str(data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['formats'][k]['VodFormatVO']['audio'] + " - " + data['ResponseVO']['categories'][i]['CategoryVO']['vodsArray'][j]['VodMovieVO']['formats'][k]['VodFormatVO']['quality'] + ";")
          k+=1

        try:
          cmd = "curl -X GET 'http://www.omdbapi.com/?t="+movieOName.replace(' ', '%20').replace("'","%27")+"' 2> /dev/null"
          o = getResponse(cmd)
          dataIMDB = json.loads(o)
          if dataIMDB['Response'] == 'True':
            movieIsIMDB = dataIMDB['Response']
            movieTitleI = dataIMDB['Title']
            movieYearI = int(str(dataIMDB['Year']).replace("\xe2\x80\x93", "")) 
            movieReleaseI = dataIMDB['Released']
            movieDirectorI = dataIMDB['Director'].replace(";",",")
            movieActorsI = dataIMDB['Actors'].replace(";",",")
            moviePlotI = dataIMDB['Plot'].replace(";",",")
            movieCountryI = dataIMDB['Country']
            movieLanguageI = dataIMDB['Language']
            movieGenreI = dataIMDB['Genre'].replace(";",",")
            if dataIMDB['imdbRating'] == 'N/A':
              movieRatingI = float(0.0)
            else:
              movieRatingI = float(dataIMDB['imdbRating'])
            if dataIMDB['imdbVotes'] == 'N/A':
              movieVotesI = int(0)
            else:
              movieVotesI = int(dataIMDB['imdbVotes'].replace(",",""))
            movieAwardsI = str(dataIMDB['Awards'].replace(";",","))
            movieImgI = str(dataIMDB['Poster'].replace(";",","))
          else:
            movieIsIMDB = dataIMDB['Response']
            movieTitleI = ""
            movieYearI = 0
            movieReleaseI = ""
            movieDirectorI = ""
            movieActorsI = "" 
            moviePlotI = ""
            movieCountryI = ""
            movieLanguageI = "" 
            movieGenreI = "" 
            movieRatingI = 0.0
            movieVotesI = 0 
            movieAwardsI = "" 
            movieImgI = "" 
  
        except Exception, e:
          if nbE == 0:
            logE += "\n" + date + "\n"
          logE += movieID + "\n"
          logE += movieName + "\n"
          logE += cmd + "\n"
          logE +=  "exception IMDB: " + str(e) + "\n"
          logE +=  o + "\n"
          nbE += 1

        try:
          me = MovieEntry(mType="MOVIE", mCat=str(catName), mNbCat=int(catNbMovies), mID=str(movieID), mTitleTP=str(movieName), mOriginalTitleTP=str(movieOName), mCountryTP=str(movieCountry), mYearTP=int(movieYear), mGenreTP=str(movieGenre), mVotesTP=int(movieVotes), mDescriptionTP=str(movieDescription.replace(';', ',')), mDirectorTP=str(movieDirector.replace(';', ',')), mActorsTP=str(movieActors.replace(';', ',')), mIMGTP=str(movieIMG), mIsIMDB=str(movieIsIMDB),mTitleI=str(movieTitleI), mYearI=int(movieYearI), mDateReleaseI=str(movieReleaseI), mDirectorI=str(movieDirectorI), mActorsI=str(movieActorsI), mDescriptionI=str(moviePlotI), mCountryI=str(movieCountryI), mLanguageI=str(movieLanguageI),mGenreI=str(movieGenreI), mRatingI=float(movieRatingI), mVotesI=int(movieVotesI), mAwardsI=str(movieAwardsI), mImgI=str(movieImgI), mFormat1=formats[0], mFormat2=formats[1], mFormat3=formats[2], mFormat4=formats[3], mFormat5=formats[4], mFormat6=formats[5], mFormat7=formats[6], mFormat8=formats[7], mNew=True, mSeen=False, mWhishlist=False, mIMDBWrong=False)
          me.save()
        except Exception, e:
          if nbE == 0:
            logE += "\n" + date + "\n"
          logE += movieID
          logE += movieName
          logE += "Exception DB: " + str(e) + "\n"
          nbE += 1

      j+=1
    i+=1

  with open('dmapp/exceptions.txt', 'a') as data_exception_file:    
    data_exception_file.write(logE)


  print str(nbE) + " exceptions"

  p = ParamEntry.objects.get(mName='isUpdating')
  p.mValue = 'false'
  p.save()

  return nbE

if __name__ == '__main__':
  getMoviesJSON()
  parseJson()
