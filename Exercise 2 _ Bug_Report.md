# Bug report
Dear Mr./Mrs.,

I present hereby a recent bug faced by our users when accessing the following webpage:
<center><span style="color:red">https://test.streamroot.io/candidates/test.html</span></center>

## Summary
After using the debugging utilities of the “graph.js” script, it was noted that the current page is not able to identify new sources with the same video in order to engage on the Peer-to-Peer data transmission.
Furthermore, it was identified through the analysis of the source code the manifestation of a “403” error type with the call of the “dna-client.js” script, as a result of the following error message:
<center><span style="color:red">GET https://cdn.streamroot.io/latest/dna-client/5.30.1/dna-client.js net::ERR_ABORTED 403</span></center>

## Steps to reproduce
The bug is manifested in the test sample when simulating the webpage access by different users, through the use of different tabs in the “Google Chrome Version 88.0.4324.146 (Official) 64 bits”. It is seen that the underlying code does not work on fetching the new video sources, and the Google Chrome console identifies the 403 error in the opened webpages.

## Expected Results
It would be expected that the program would respond to the access of different users to the video content with the increment of the “Sources” variable, and by starting the P2P service to offload the usage of CDN bandwidth.

![Expected Results](https://github.com/henriquewills/Intern-Test/tree/main/images/bug_absent.jpg)
## Actual Results
The bug could be identified by the amount of offload and the number of sources identified by the debugging utility, which are found to be respectively 0.0% and 0 sources regardless of the number of additional peers that are accessing the same content.

![Actual Results](https://github.com/henriquewills/Intern-Test/tree/main/images/bug_present.jpg)
![Error 403](https://github.com/henriquewills/Intern-Test/tree/main/images/Error_403.jpg)
## Notes
It was checked that the upload instance was set as TRUE in all of the opened webpages.

![Upload allowed](https://github.com/henriquewills/Intern-Test/tree/main/images/Upload_allowed.jpg)

Cordially,

Henrique Wills
