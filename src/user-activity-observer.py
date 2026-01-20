class UserActivityObserver(LogObserver):
    
    def update(self, log_analyzer : 'LogAnalyzer') -> None:
        compiled_re = re.compile(r'[Uu]ser')
        for s in strings :
            if compiled_re.search(s):
                print(f"User activity found in : {s}")