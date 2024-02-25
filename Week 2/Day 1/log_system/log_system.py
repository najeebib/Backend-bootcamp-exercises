from datetime import datetime


def log_factory():
    def log(message, timestamp=False, log_level=None, events=None):
        log_message = {"message": message}

        if timestamp:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message["timestamp"] = time_now
        
        if log_level:
            log_message["log_level"] = log_level
        
        if events:
            log_message["events"] = events
            date_now = datetime.now().strftime("%Y-%m-%d")
            log_message["date"] = date_now

        return log_message

    return log
create_log = log_factory()


def log_processing_factory():
    def process_logs(logs, filters_dict):
        
        filtered = []
        for log in logs:
            no_timestamp = True
            in_range = True
            short = True
            if filters_dict.get("no_timestamp") and "timestamp" in log:
                no_timestamp = False
            if filters_dict.get("timestamp_range") and "timestamp" in log:
                start_time, end_time = filters_dict["timestamp_range"]
                timestamp = datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S")
                if start_time > timestamp  or timestamp > end_time:
                    in_range = False

            if filters_dict.get("short_message") and len(log["message"]) >= 10: 
                short = False
            if no_timestamp and in_range and short:
                filtered.append(log)

        return filtered
        
    return process_logs
            
logs = [
    create_log("short"),
    create_log("Log message with timestamp", timestamp=True),
    create_log("Log message with timestamp and log level", timestamp=True, log_level="warn"),
    create_log("looooooooooooooooooooong", events=["event1", "event2"]),
]
for log in logs:
    print("timestamp" in log)
log_processor = log_processing_factory()

filter_dictionary = {
    "no_timestamp": True,
    "short_message": False
}

log_processor = log_processing_factory()
filtered = log_processor(logs, filter_dictionary)

print((filtered))