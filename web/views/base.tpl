<!DOCTYPE html>
<html>
<head>
<title>{{title or "Derp"}} | Interlock Doorberry</title>

<link rel="stylesheet" href="/css/bootstrap.min.css" media="screen">

</head>
<body>
%if defined('note'):
<div id="note">{{note}}</div>
%end

<div id="content">
%include
</div>

<script src="http://code.jquery.com/jquery-latest.js"></script>
<script src="/js/bootstrap.min.js"></script>
</body>
</html>
