# MySpeedyFuzzer
A really speedy Fuzzing program, working with multithreading<br>
© Andrea Fecchio, Performance Evaluation Group, UniPV, 2019<br><br>

Run main routine from fuzzer.py.<br>
Usage:<br>
  PROG_NAME [-h] -u URL -t CONCURRENCY -l FILELIST [FILELIST ...] [-d DATA]<br><br>

Arguments:<br>
  -h, --help      --> show this help message and exit<br>
  -u URL, --url URL     --> the url of the web app to be tested, with "{}" for payloads (in case GET)<br>
  -t CONCURRENCY, --concurrency CONCURRENCY     --> max number of concurrent HTTP requests<br>
  -l FILELIST, --filelist FILELIST    --> input .txt file(s), containing one payload per line<br>
  -d DATA, --data DATA    --> key-value couple (indicated: "key={}") staying for the parameter to be found (only in case POST)<br><br>
  
  Limitations:<br>
    - only working with GET, POST requests<br>
    - only working with one parameter<br>
