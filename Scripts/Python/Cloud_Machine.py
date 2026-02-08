import datetime
import time

class CloudMachine:
    def __init__(self, provider_id):
        self.provider_id = provider_id
        self.start_time = None
        self.total_cost = 0

    def start(self):
        self.start_time = datetime.datetime.now()
        print(f"Machine started at {self.start_time}")

    def stop(self):
        if not self.start_time:
            return 0
        
        duration = datetime.datetime.now() - self.start_time
        minutes = duration.total_seconds() / 60
        
        # Rate per minute: Provider 1 = $2, Others = $5
        rate = 2 if self.provider_id == 1 else 5
        cost = minutes * rate
        self.total_cost += cost
        return cost

if __name__ == '__main__':
    vm = CloudMachine(provider_id=1)
    vm.start()
    time.sleep(2) # Simulating activity
    print(f"Usage cost: ${vm.stop():.2f}")
