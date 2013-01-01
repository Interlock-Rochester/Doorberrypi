<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Index | Interlock Doorberry</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">

    <!-- Le styles -->
    <link href="/css/bootstrap.css" rel="stylesheet">
    <link href="/css/font-awesome.css" rel="stylesheet">
    <style type="text/css">
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }
    </style>
    <link href="/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <script language="javascript" type="text/javascript">

      var wsUri = "ws://localhost:8080/logsocket";
      var output;

      function init()
      {
        output = document.getElementById("output");
        testWebSocket();
      }

      function testWebSocket()
      {
        websocket = new WebSocket(wsUri);
        websocket.onopen = function(evt) { onOpen(evt) };
        websocket.onclose = function(evt) { onClose(evt) };
        websocket.onmessage = function(evt) { onMessage(evt) };
        websocket.onerror = function(evt) { onError(evt) };
      }

      function onOpen(evt)
      {
        writeToScreen("CONNECTED");
        doSend("WebSocket rocks");
      }

      function onClose(evt)
      {
        writeToScreen("DISCONNECTED");
      }

      function onMessage(evt)
      {
        writeToScreen('<span style="color: blue;">RESPONSE: ' + evt.data+'</span>');
        websocket.close();
      }

      function onError(evt)
      {
        writeToScreen('<span style="color: red;">ERROR:</span> ' + evt.data);
      }

      function doSend(message)
      {
        writeToScreen("SENT: " + message); 
        websocket.send(message);
      }

      function writeToScreen(message)
      {
        var pre = document.createElement("p");
        pre.style.wordWrap = "break-word";
        pre.innerHTML = message;
        output.appendChild(pre);
      }

      window.addEventListener("load", init, false);

    </script>

  </head>
  <body>

  <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">Interlock Doorberry Pi</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="#">Index</a></li>
              <li><a href="#">Logs</a></li>
              <li><a href="#">Ponies</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
  </div>

<div class="container">
<div class="row">
  <div class="span6">
   <div class="navbar">
  <div class="navbar-inner">
    <a class="brand" href="#">Keys</a>
    <ul class="nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Link</a></li>
      <li><a href="#">Link</a></li>
    </ul>
  </div>
</div>
    <p>This is the index, dummy.</p>
  </div>
  <div class="span6">
<div class="navbar">
  <div class="navbar-inner">
    <a class="brand" href="#">Logs</a>
    <ul class="nav">
      <li class="active"><a href="#">Home</a></li>
      <li><a href="#">Link</a></li>
      <li><a href="#">Link</a></li>
    </ul>
  </div>
</div>
    <div id="output"></div>
  </div>
</div>

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/js/jquery.js"></script>
    <script src="/js/bootstrap.min.js"></script>
  </body>
</html>
