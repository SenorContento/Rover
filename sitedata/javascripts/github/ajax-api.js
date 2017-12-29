/* The whole point of this file is to allow me to use the Github API in order to perform authentication when editing blog posts on my 
 * website. After performing authentication, I will have my own Javascript editor to make changes to my site live before pushing to 
 * Github. If I set the Javascript correctly, I can also build an on phone editor on both the website and app that will allow me to 
 * edit my posts on the fly. The main reason for doing this is so I can visually see what posts in the _drafts folder look like instead 
 * of it just being a mental image or having to wait until I get home.
 *
 * I give other people permission to use this file or files if more than one file in this directory in their projects as long as they 
 * credit the original author (Señor Contento). (C) 2015 CubeTech, LLC
 *
 *                                         This project is currently coded for Github API v3                                         */

var username, password, rateLimitCore, rateLimitSearch, data = "";
var url = "https://api.github.com/";
var method = "GET";

function lookup() {
  if(url != "https://api.github.com/rate_limit") {
    var useurl = url;
    var usemethod = method;
    method = "GET";
    url = "https://api.github.com/rate_limit";
    var rawJSON = lookup();
    var rateLimit = $.parseJSON(lookup());
    /* Those vars are "remaining" which are in "core" and "search" and not "rate" which will be deprecated in the next api */
    jQuery.each(rateLimit, function(index, item) {
        if(item instanceof Object) {
          recurseRateLimit(index, item);
        } else {
          /* alert(index + " | " + item); This should never occur unless Github changes the output of the rateLimit page. */
        }
    });
    url = useurl;
    method = usemethod;
    /* This is used to make sure the rate limit does not reset the counter. */
    /* Searches do not count against the normal rate limit*/
    if(rateLimitCore == 0 && url.indexOf("q=") == -1) {
      alert("You have reached your rate limit for general use on the Github API, please wait an hour!");
      return "General Rate Limit Used Up!";
    }
    else if(rateLimitSearch == 0 && url.indexOf("q=") > -1) {
      alert("You have reached your rate limit for searches on the Github API, please wait an hour!");
      return "Search Rate Limit Used Up!";
    }
  }
  var returnvalue;
  $.ajax({
    url: url,
    type: method,
    async: false,
    data: data,
    beforeSend: function(xhr) {
      /* xhr means XMLHttpRequest */
      xhr.setRequestHeader("Accept", "application/vnd.github.v3+json");
      if(typeof username != "undefined" && typeof password != "undefined") {
        if(username != "" && password != "") {
          xhr.setRequestHeader("Authorization", "Basic " + btoa(username + ":" + password));
        }
      }
    }, error: function(data, status, thrown) {
      /* data is the exact same thing as data in complete, but with bad error codes
       * status throws out error, just like how status in complete throws out success
       * thrown tells what type of error it is */
      /*if(thrown == "Unauthorized") {
        alert("You either typed in an invalid username or password or did not type one at all! Did you try tokens?");
      } else if(thrown == "Not Found") {
        alert("It appears the info you were looking found was not found!");
      } else if(thrown == "Unprocessable Entity") {
        alert("Sorry, the server was not able to process your request!");
      } else if(thrown == "Bad Request") {
        alert("You have sent a bad request!");
      } else if(thrown == "Forbidden") {
        alert("Sorry, you are not allowed to access this resource!");
      } else if(thrown == "") {
        alert("Sorry, the error is unknown, possibly a bad url?");
      } else {
        alert("There was an error with this http request! Error is \"" + thrown + "\"");
      }*/ /* The above are useful messages, but I may use the json responses instead for more accurate messages and for a nicer method of presenting messages */
      returnvalue = JSON.stringify(data);
    }, success: function(data) {
      //$('#login').submit(); //This allows the Save Password Dialog to show in FF. Does not work in Chrome, causes page refresh.
      returnvalue = JSON.stringify(data);
    }, complete: function(data, status) {
      /* data is same as data in success, but with error codes and status messages thrown in with it
       * status is the status message without any other data. status is by default a string, not json */
      /* alert(JSON.stringify(data) + " | " + status); */
    }
  });
  return returnvalue;
}
function recurseRateLimit(key, value) {
  $(document).ready(function() {
    if(value instanceof Object) {
      $.each(value, function(k, v) {
        if(v instanceof Object) {
          recurseRateLimit(k, v);
        } else {
          if(k == "remaining") {
            //alert(key + " | " + v);
            if(key == "core")
            {
              rateLimitCore = v;
            }
            else if(key == "search") {
              rateLimitSearch = v;
            }
          }
        }
      });
    }
  });
}
