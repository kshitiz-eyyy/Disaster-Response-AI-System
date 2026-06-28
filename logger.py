import csv
import datetime

def log_path(test_name, path_length, execution_time):
    file_name = "performance_log.csv"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Timestamp", "Test Name", "Path Length", "Execution Time (sec)"])
        writer.writerow([timestamp, test_name, path_length, execution_time])