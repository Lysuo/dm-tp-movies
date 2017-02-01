var wsDic = {};
var fieldsWS = {};
var memTable = {};

var i = 0;
var count = 0;
var movieSelectedK;

var countries = ["Dinamarca","Estados Unidos","Gran Bretaña","Italia","Argentina","Israel","Canadá","México","Noruega","Chile","Brasil","Francia","Corea del Sur","Japón","Sudáfrica","Alemania","Reino Unido","Australia","China","España","Corea del Norte","India","Taiwán","Suecia","República Dominicana","República Checa","Afganistán","Nueva Zelanda","Ruanda"];
countries.sort();
console.log(countries);

var categories = ["Infantiles y familiares","Drama","Comedia","Acción y Aventura","Documentales","Terror y Suspenso","Estreno","Para ti","Para empezar bien el año","Música","Romance","Lista de deseos","Películas Mexicanas","Clásicos","3D"];
var action = 'get_movies';

$(function(){

  wsDic["year"] = {"dbName": "mYearTP", "pred": {"type": "select", "display": [">", "<", "="], "values": ["__gt", "__lt", ""]}, "value": {"form": "int", "type": "input", "values": ["2016"]}};
  wsDic["rating"] = {"dbName": "mRatingI", "pred": {"type": "select", "display": [">", "<", "="], "values": ["__gt", "__lt", ""]}, "value": {"form": "float", "type": "input", "values": ["7.0"]}};
  wsDic["title"] = {"dbName": "mOriginalTitleTP", "pred": {"type": "select", "display": ["contains"], "values": ["__contains"]}, "value": {"form": "string", "type": "input", "values": ["potter"]}};
  wsDic["country"] = {"dbName": "mCountryTP", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "string", "type": "select", "values": countries, "display": countries}};
  //wsDic["country"] = {"dbName": "mCountryTP", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "string", "type": "input", "values": ["Estados Unidos"]}};
  wsDic["catgory"] = {"dbName": "mCat", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "string", "type": "select", "values": categories, "display": categories}};
  wsDic["isNew"] = {"dbName": "mNew", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "boolean", "type": "input", "values": ["True", "False"]}};
  wsDic["isWhishlist"] = {"dbName": "mWhishlist", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "boolean", "type": "input", "values": ["True", "False"]}};
  wsDic["isSeen"] = {"dbName": "mSeen", "pred": {"type": "select", "display": ["is"], "values": [""]}, "value": {"form": "boolean", "type": "input", "values": ["False", "True"]}};
  
  
  for (var k in wsDic) {
    $('#ws-list').append("<option>"+k+"</option>");
  }


});

function dealEvent(event) {

  var input;
  var html = "";

  if (event!=null) {		
    if(event.target.id == "pred") {
      fieldsWS[event.target.id] = $("#"+event.target.id+" option:selected").text();
      if ($("#"+event.target.id+" option:selected").val() == undefined) {
        fieldsWS[event.target.id] = $("#"+event.target.id).text();
      }
    } else if(event.target.id == "value") {
      fieldsWS[event.target.id] = $("#"+event.target.id+" option:selected").val();
      if ($("#"+event.target.id+" option:selected").val() == undefined) {
        fieldsWS[event.target.id] = $("#"+event.target.id).val();
      }
    }
  }

  if ($("#ws-list option:selected").text() != "----------") {
    html += $("#server-list option:selected").val();
    html += wsDic[$("#ws-list option:selected").text()]["type"] + "?type=" + $("#ws-list option:selected").text();		
  }
}


$('#ws-list').change(function() {
  fieldsWS = {};
  $('#dyn-form').empty();

  var val = $("#ws-list option:selected").text();


  var dic = wsDic[val];
  var html = "";

  for (var key in dic) {
    html += "<br/>";
    if (dic[key]["type"] == "input") {

      html += "<label for=\""+key+"\">"+key+"</label><br/>";
      html += "<input type=\"text\" id=\""+key+"\" value=\""+dic[key]["values"][0]+"\" onchange=\"dealEvent(event);\"><br/>";
      fieldsWS[key] = dic[key]["values"][0];

    } else if (dic[key]["type"] == "select") {
      html += "<label for=\""+key+"\">"+key+"</label><br/>";
      html += "<select id=\""+key+"\" onchange=\"dealEvent(event);\">";
      for (var e in dic[key]["values"]) {
		//console.log(dic[key]["values"][e]);
        html += "<option value=\""+dic[key]["values"][e]+"\">"+dic[key]["display"][e]+"</option>";
        fieldsWS[key] = dic[key]["display"][0];
      }
      html += "</select><br/>";

    }		
  }

  $('#dyn-form').append(html);

});

$('#add-filter-button').click(
    function () {
      console.log("add filter button clicked");
      console.log(fieldsWS);

      var key = $("#ws-list option:selected").text();

      var html = "";
      html += "<tr id=\"filter-"+parseInt(count)+"\">";
      html += "<td>"+$("#ws-list option:selected").text()+"</td>";
      html += "<td>"+fieldsWS["pred"]+"</td>";
      html += "<td>"+fieldsWS["value"]+"</td>";
      html += "<td>"+"<input id=\"delete-filter-"+parseInt(count)+"\" type=\"button\" value=\"X\" onclick=\"deleteFilter(event)\"/>"+"</td>";
      html += "</tr>";		

      var val = fieldsWS["value"];
      var valF;
      if (wsDic[key]["value"]["form"] == "int") {
        valF = parseInt(val);
      } else if (wsDic[key]["value"]["form"] == "float") {
        valF = parseFloat(val);
      } else if (wsDic[key]["value"]["form"] == "boolean") {
        valF = (val === 'True');
      } else {
        valF = val
      }

      memTable[count] = [wsDic[key]["dbName"] + $("#pred option:selected").val(), valF];
      count += 1;

      appendTable(html);
    });




function deleteFilter(event) {
  console.log("delete button clicked " + event.target.id);
  var idFilter = (event.target.id).replace('delete-filter-', '');
  $("#filter-"+idFilter).remove();
  delete memTable[parseInt(idFilter)];
  console.log(memTable);
}

function appendTable(html) {
  $('#result-table').append(html);
}

$('.ws-fields').change(function(event) {
  dealEvent(event);
});

var dataToSend = {
  'filters' : [
    'mYearTP__gte',
  2016
    ], 
  'action': 'get_movies',
};

var arrResults = [];

$("#table-results").delegate('tr', 'click', function() {
	
  $('#button-save-movie-changes').attr("style", "");
  
  var html = '<br /><br /><br /><table style="width:100%">'; //<tr><th></th><th>TP</th><th>IMDB</th></tr>'
  var k = parseInt($(this).attr("name"));
  movieSelectedK = k;

  html += '<tr><td><b>ID</b></td><td id="id-movie-selected" value='+arr[k].mId+'>'+arr[k].mId+'</td><td></td></tr>';
  html += '<tr><td><b>Title</b></td><td>'+arr[k].mTitleTP+'</td><td></td></tr>';
  html += '<tr><td><b>Original Title</b></td><td>'+arr[k].mOriginalTitleTP+'</td><td>'+arr[k].mTitleI+'</td></tr>';
  html += '<tr><td><b>Category</b></td><td>'+arr[k].mCat+'</td><td></td></tr>';
  html += '<tr><td><b>Genre</b></td><td>'+arr[k].mGenreTP+'</td><td>'+arr[k].mGenreI+'</td></tr>';
  html += '<tr><td><b>Director</b></td><td>'+arr[k].mDirectorTP+'</td><td>'+arr[k].mDirectorI+'</td></tr>';
  html += '<tr><td><b>Actors</b></td><td>'+arr[k].mActorsTP+'</td><td>'+arr[k].mActorsI+'</td></tr>';
  html += '<tr><td><b>Year</b></td><td>'+arr[k].mYearTP+'</td><td>'+arr[k].mYearI+'</td></tr>';
  html += '<tr><td><b>Date</b></td><td></td><td>'+arr[k].mDateReleaseI+'</td></tr>';
  html += '<tr><td><b>Country</b></td><td>'+arr[k].mCountryTP+'</td><td>'+arr[k].mCountryI+'</td></tr>';
  html += '<tr><td><b>Rating</b></td><td></td><td>'+arr[k].mRatingI+'</td></tr>';
  html += '<tr><td><b>Votes</b></td><td>'+arr[k].mVotesTP+'</td><td>'+arr[k].mVotesI+'</td></tr>';
  html += '<tr><td><b>Awards</b></td><td></td><td>'+arr[k].mAwardsI+'</td></tr>';
  html += '</table><br /><br />';

  html += "<b>Formats</b>: " + arr[k].mFormat1 + " ; ";
    html += arr[k].mFormat2 + " ; ";
    html += arr[k].mFormat3 + " ; ";
    html += arr[k].mFormat4 + " ; ";
    html += arr[k].mFormat5 + " ; ";
    html += arr[k].mFormat6 + " ; ";
    html += arr[k].mFormat7 + " ; ";
    html += arr[k].mFormat8 + " ; <br /><br /> ";

    html += "<b>Description TP</b>:" + arr[k].mDescriptionTP + "<br /><br />";
    html += "<b>Description IMDB</b>:" + arr[k].mDescriptionI + "<br /><br />";

    $("#div-content-movie").html("");
  $("#div-content-movie").append(html);
  
  if (arr[k].mNew) {
	$('#isNewCheckbox').prop('checked', true);
  } else {
	$('#isNewCheckbox').prop('checked', false);
  }
  if (arr[k].mSeen) {
	$('#isSeenCheckbox').prop('checked', true);
  } else {
	$('#isSeenCheckbox').prop('checked', false);
  }
  if (arr[k].mWhishlist) {
	$('#isWhishListCheckbox').prop('checked', true);
  } else {
	$('#isWhishListCheckbox').prop('checked', false);
  }
  $("#checkboxes-div").attr("style", "display:visible;");
});

$(window).scroll(function() { 
  //console.log("scroll function");
  //console.log($(this).scrollTop());
  $('#div-content-movie').css('marginTop', $(window).scrollTop()-25 + "px");
});

$('#button-test').click(
    function () {
      console.log("submit button clicked");
      //console.log(memTable);

      var filters = [];
      var i = 0;
      while (i<count) {
        if (i in memTable) {
          filters.push(memTable[i][0]);
          filters.push(memTable[i][1]);
        }
        i+=1;
      }
	  action = 'get_movies';

      console.log(filters);	
      dataToSend = { 'filters' : filters, 'action': action };

      $.ajax({
        type: 'POST' ,
        cache: false,
        url: '/',
        datatype: "json",
        async: true,
        data: dataToSend,

        success: function(json) {

          arr = [];
          $('#table-results').html('');

          arr = $.parseJSON(json);
          console.log(arr);


          var html = '';
          html += arr.length + ' results <br /><br />';
          html += '<table style="width:100%"><tr><th>Title</th></tr>';
          $.each(arr, function(i, item){
            html += '<tr name="'+i+'"><td>'+item.mOriginalTitleTP+'</td></tr>';
          });
          html += '</table><br /><br />';

          $('#table-results').append(html);

          console.log("success");
        },
        error: function(){
          console.log("error");
        }, 
        complete: function(){
          console.log("complete");
        } 
      });
    });
	
	
$('#update-button').click(
	function () {
      console.log("update button clicked");

      var filters = [];      
	  action = 'run_update';
	  var session = $('#input-session-TP').val();
	  console.log(session);
	  
      dataToSend = { 'filters' : filters, 'action': action, 'sessionTP': session };

      $.ajax({
        type: 'POST' ,
        cache: false,
        url: '/',
        datatype: "json",
        async: true,
        data: dataToSend,

        success: function(json) {        
          console.log(json);
          console.log("success");
        },
        error: function(){
          console.log("error");
        }, 
        complete: function(){
          console.log("complete");
        } 
		});
});

$('#button-save-movie-changes').click(
	function () {
      console.log("save movie changes button clicked");

	  action = 'save_changes';
	  
      dataToSend = { 
		'action': action,
		'idMovie': $('#id-movie-selected').html(),
		'isNew': $('#isNewCheckbox').is(':checked'),
		'isSeen': $('#isSeenCheckbox').is(':checked'),
		'isWhishlist': $('#isWhishListCheckbox').is(':checked')
	  };

	  
      $.ajax({
        type: 'POST' ,
        cache: false,
        url: '/',
        datatype: "json",
        async: true,
        data: dataToSend,

        success: function(json) {
          console.log("success");
		  arr[movieSelectedK].mNew = dataToSend['isNew'];
		  arr[movieSelectedK].mSeen = dataToSend['isSeen'];
		  arr[movieSelectedK].mWhishlist = dataToSend['isWhishlist'];
		  $('#button-save-movie-changes').attr("style", "background-color:green;");
        },
        error: function(){
          console.log("error");		  
		  $('#button-save-movie-changes').attr("style", "background-color:red;");
        }, 
        complete: function(){
          console.log("complete");
        } 
		});
});

function checkUpdateStatus(){

	action = 'check_update';
	dataToSend = {'action': action};
	
	

      $.ajax({
        type: 'POST' ,
        cache: false,
        url: '/',
        datatype: "json",
        async: true,
        data: dataToSend,

        success: function(json) {        
          console.log("checkUpdate: " + json);
          //console.log("success");
        },
        error: function(){
          console.log("error");
        }, 
        complete: function(){
          //console.log("complete");
        } 
		});
		
    setTimeout(checkUpdateStatus, 5000);
}

//checkUpdateStatus();	
	
