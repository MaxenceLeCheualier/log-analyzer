class ErrorObserver(LogObserver): 

    def update(self, log_analyzer : 'LogAnalyzer') -> None:
        compiled_re = re.compile(r'ERROR')
        for s in strings :
            if compiled_re.search(s):
                print(f"Error found in : {s}")
