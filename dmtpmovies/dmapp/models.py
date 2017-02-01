from __future__ import unicode_literals
from django.db import models

# Create your models here.

class ParamEntry(models.Model):
  mName = models.CharField(max_length=50)
  mValue = models.CharField(max_length=200)
  def __unicode__(self):
    return self.mName

class MovieEntry(models.Model):
  mType = models.CharField(max_length=200)
  mCat = models.CharField(max_length=200)
  mNbCat = models.IntegerField()
  mID = models.CharField(max_length=200)
  mTitleTP = models.CharField(max_length=200)
  mOriginalTitleTP = models.CharField(max_length=200)
  mCountryTP = models.CharField(max_length=200)
  mYearTP = models.IntegerField()
  mGenreTP = models.CharField(max_length=200)
  mVotesTP = models.IntegerField()
  mDescriptionTP = models.CharField(max_length=200)
  mDirectorTP = models.CharField(max_length=200)
  mActorsTP = models.CharField(max_length=200)
  mIMGTP = models.CharField(max_length=250)
  mIsIMDB = models.BooleanField(default=False)
  mTitleI = models.CharField(max_length=200, blank=True)
  mYearI = models.IntegerField(blank=True)
  mDateReleaseI = models.CharField(max_length=200, blank=True)
  mDirectorI = models.CharField(max_length=200, blank=True)
  mActorsI = models.CharField(max_length=200, blank=True)
  mDescriptionI = models.CharField(max_length=200, blank=True)
  mCountryI = models.CharField(max_length=200, blank=True)
  mLanguageI = models.CharField(max_length=200, blank=True)
  mGenreI = models.CharField(max_length=200, blank=True)
  mRatingI = models.FloatField(blank=True)
  mVotesI = models.IntegerField(blank=True)
  mAwardsI = models.CharField(max_length=200, blank=True)
  mImgI = models.CharField(max_length=200, blank=True)
  mFormat1 = models.CharField(max_length=200)
  mFormat2 = models.CharField(max_length=200, blank=True)
  mFormat3 = models.CharField(max_length=200, blank=True)
  mFormat4 = models.CharField(max_length=200, blank=True)
  mFormat5 = models.CharField(max_length=200, blank=True)
  mFormat6 = models.CharField(max_length=200, blank=True)
  mFormat7 = models.CharField(max_length=200, blank=True)
  mFormat8 = models.CharField(max_length=200, blank=True)
  mNew = models.BooleanField(default=True)
  mSeen = models.BooleanField(default=False)
  mWhishlist = models.BooleanField(default=False)
  mIMDBWrong = models.BooleanField(default=False)
  mDateUpdate = models.DateTimeField(auto_now_add=True, auto_now=False)

  def __unicode__(self):
    return self.mOriginalTitleTP

  def as_dict(self):
    return {
        "id": self.id,
        "mType": self.mType.encode('utf8'),
        "mCat": self.mCat.encode('utf8'),
        "mId": self.mID.encode('utf8'),
        "mTitleTP": self.mTitleTP.encode('utf8'),
        "mOriginalTitleTP": self.mOriginalTitleTP.encode('utf8'),
        "mCountryTP": self.mCountryTP.encode('utf8'),
        "mYearTP": self.mYearTP,
        "mGenreTP": self.mGenreTP.encode('utf8'),
        "mVotesTP": self.mVotesTP,
        "mDescriptionTP": self.mDescriptionTP.encode('utf8'),
        "mDirectorTP": self.mDirectorTP.encode('utf8'),
        "mActorsTP": self.mActorsTP.encode('utf8'),
        "mIMGTP": self.mIMGTP.encode('utf8'),
        "mIsIMDB": self.mIsIMDB,
        "mTitleI": self.mTitleI.encode('utf8'),
        "mYearI": self.mYearI,
        "mDateReleaseI": self.mDateReleaseI.encode('utf8'),
        "mDirectorI": self.mDirectorI.encode('utf8'),
        "mActorsI": self.mActorsI.encode('utf8'),
        "mDescriptionI": self.mDescriptionI.encode('utf8'),
        "mCountryI": self.mCountryI.encode('utf8'),
        "mLanguageI": self.mLanguageI.encode('utf8'),
        "mGenreI": self.mGenreI.encode('utf8'),
        "mRatingI": self.mRatingI,
        "mVotesI": self.mVotesI,
        "mAwardsI": self.mAwardsI.encode('utf8'),
        "mImgI": self.mImgI.encode('utf8'),
        "mFormat1": self.mFormat1.encode('utf8'),
        "mFormat2": self.mFormat2.encode('utf8'),
        "mFormat3": self.mFormat3.encode('utf8'),
        "mFormat4": self.mFormat4.encode('utf8'),
        "mFormat5": self.mFormat5.encode('utf8'),
        "mFormat6": self.mFormat6.encode('utf8'),
        "mFormat7": self.mFormat7.encode('utf8'),
        "mFormat8": self.mFormat8.encode('utf8'),
        "mNew": self.mNew,
        "mSeen": self.mSeen,
        "mWhishlist": self.mWhishlist,
        "mIMDBWrong": self.mIMDBWrong,
        }
