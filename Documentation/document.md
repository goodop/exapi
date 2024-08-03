# API Documentation

Welcome to the API documentation for **Exapi**. Below you'll find a list of available endpoints along with their parameters.

## Endpoints and Parameters

Host:
```bash
https://execross.com/api/v3
```

<div style="overflow-x:auto; white-space: nowrap;">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
  <thead>
    <tr>
      <th style="text-align: left; padding: 8px; width: 10%;">No.</th>
      <th style="text-align: left; padding: 8px; width: 30%;">Endpoint</th>
      <th style="text-align: left; padding: 8px; width: 60%;">Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px;">1</td>
      <td style="padding: 8px;">/proxies</td>
      <td style="padding: 8px;">None</td>
    </tr>
    <tr>
      <td style="padding: 8px;">2</td>
      <td style="padding: 8px;">/loginqr</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - proxy
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">3</td>
      <td style="padding: 8px;">/reqpin</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">4</td>
      <td style="padding: 8px;">/reqtoken</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">5</td>
      <td style="padding: 8px;">/loginqrv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - proxy
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">6</td>
      <td style="padding: 8px;">/reqpinv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">7</td>
      <td style="padding: 8px;">/reqtokenv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - session
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">8</td>
      <td style="padding: 8px;">/loginemail</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - email<br>
        - password<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">9</td>
      <td style="padding: 8px;">/reqemailtoken</td>
      <td style="padding: 8px;">
        - apikey
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">10</td>
      <td style="padding: 8px;">/loginemailv1</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - certificate<br>
        - email<br>
        - password<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">11</td>
      <td style="padding: 8px;">/reqemailtokenv1</td>
      <td style="padding: 8px;">
        - apikey
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">12</td>
      <td style="padding: 8px;">/addfriend</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">13</td>
      <td style="padding: 8px;">/linestory</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">14</td>
      <td style="padding: 8px;">/linepost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - mid<br>
        - postId
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">15</td>
      <td style="padding: 8px;">/friendrecomendation</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">16</td>
      <td style="padding: 8px;">/msgidtourl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - appName<br>
        - authToken<br>
        - proxy (optional)<br>
        - messageId
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">17</td>
      <td style="padding: 8px;">/convertparseurl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - parseURL
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">18</td>
      <td style="padding: 8px;">/webp2mp4</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">19</td>
      <td style="padding: 8px;">/mp42gif</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url<br>
        - start<br>
        - end<br>
        - transparent (optional)
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">20</td>
      <td style="padding: 8px;">/video2apng</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url<br>
        - start<br>
        - end
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">21</td>
      <td style="padding: 8px;">/smulepost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">22</td>
      <td style="padding: 8px;">/instapost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">23</td>
      <td style="padding: 8px;">/instastory</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">24</td>
      <td style="padding: 8px;">/instastalker</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">25</td>
      <td style="padding: 8px;">/instaprofiledetails</td>
      <td style="padding: 8px;">
        - apikey<br>
        - userid
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">26</td>
      <td style="padding: 8px;">/getxpost</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">27</td>
      <td style="padding: 8px;">/facebookdl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
    <tr>
      <td style="padding: 8px;">28</td>
      <td style="padding: 8px;">/tiktokdl</td>
      <td style="padding: 8px;">
        - apikey<br>
        - url
      </td>
    </tr>
  </tbody>
</table>
</div>
