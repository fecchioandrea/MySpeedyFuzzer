# MySpeedyFuzzer
[A really speedy Fuzzing program, working with multithreading]<br><br>
It is a Python-based fuzzer, developed to discover vulnerabilities during web application security assessments. The fuzzer was inspired by the Burp "Intruder" tool, but leverages multi-threading to obtain faster performance with respect to the community edition of Burp. The project has a small codebase and it's fully open-source, to allow other developers to easily write extensions or modify it.<br><br>
© Andrea Fecchio, Performance Evaluation Group, UniPV, 2019<br><br><br>
Run main routine from fuzzer.py.<br>
Usage:<br>
  python3 fuzzer.py [-h] -u URL -t CONCURRENCY -l FILELIST [FILELIST ...] [-d DATA]<br><br>

Arguments:<br>
  -h, --help      --> show this help message and exit<br>
  -u URL, --url URL     --> the url of the web app to be tested (with "{}" for payloads, in case GET)<br>
  -t CONCURRENCY, --concurrency CONCURRENCY     --> max number of concurrent HTTP requests<br>
  -l FILELIST, --filelist FILELIST    --> input .txt file(s), containing one payload per line<br>
  -d DATA, --data DATA    --> key-value couple (indicated: "key={}") staying for the parameter to be found (only in case POST)<br><br>
  
  Limitations:<br>
    - only working with GET, POST requests<br>
    - only working with one parameter<br>
