from log-observer import LogObserver

class LogAnalyzer():
    
    def __init__(self)):
        super().__init__()
        self._observers : list[LogObserver] = []

    def observers(self) -> list['LogObserver'] : 
        return self._observers 

    def attach_obs(self, obs : 'LogObserver') -> None : 
        if obs not in self._observers : 
            self._observers.append(obs)
    
    def detach_obs(self, obs : 'LogObserver') -> None :
        self._observers.remove(obs)

    def notify_obs(self) -> None :
        for obs in self._observers :
            obs.update(self)

    def analyze_line(self) -> None : 
        self.notify_obs()


