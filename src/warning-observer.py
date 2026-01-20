class WarningObserver(LogObserver):
    
    def update(self, log_analyzer : 'LogAnalyzer') -> None:
        compiled_re = re.compile(r'WARNING')
        for s in strings :
            if compiled_re.search(s):
                print(f"Warning found in : {s}")