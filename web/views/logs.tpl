<table border="1">
<tr><td>iButton</td><td>Date/Time</td></tr>
%for x in tr:
  <tr><td>{{x[0]}}</td><td>{{x[1]}}</td></tr>
%end
</table>
%rebase base title='Logs'
