from datetime import datetime, timedelta

projects, team_members, tasks, time_logs = {}, {}, {}, []


def create_project(pid, name, start, end, priority):
    projects[pid] = {"name": name, "start": start, "end": end, "priority": priority, "tasks": [], "members": []}

def add_team_member(mid, name, role, skills, rate):
    team_members[mid] = {"name": name, "role": role, "skills": skills, "rate": rate, "tasks": [], "available": True}

def create_task(tid, pid, title, desc, est):
    tasks[tid] = {"pid": pid, "title": title, "desc": desc, "est": est, "deps": [], "progress": 0,
                  "logs": [], "actual": 0, "spent": 0, "member": None}
    projects[pid]["tasks"].append(tid)

def assign_task(tid, mid, priority):
    if not team_members[mid]["available"]: raise Exception("Unavailable member")
    tasks[tid].update({"member": mid, "priority": priority})
    team_members[mid]["tasks"].append(tid)
    if mid not in projects[tasks[tid]["pid"]]["members"]:
        projects[tasks[tid]["pid"]]["members"].append(mid)

def set_task_dependency(tid, depends_on):
    def has_cycle(t, visited=set()):
        if t in visited: return True
        visited.add(t)
        return any(has_cycle(d, visited) for d in tasks[t]["deps"])
    tasks[tid]["deps"].append(depends_on)
    if has_cycle(tid): tasks[tid]["deps"].remove(depends_on); raise Exception("Circular dependency!")

def log_time(mid, tid, hours, date):
    tasks[tid]["logs"].append({"mid": mid, "hrs": hours, "date": date})
    time_logs.append({"mid": mid, "tid": tid, "hrs": hours, "date": date})
    tasks[tid]["actual"] += hours
    tasks[tid]["spent"] += team_members[mid]["rate"] * hours

def update_task_progress(tid, pct): tasks[tid]["progress"] = pct

def calculate_project_health(pid):
    t = projects[pid]["tasks"]
    total = len(t); c = sum(tasks[i]["progress"] == 100 for i in t)
    ip = sum(0 < tasks[i]["progress"] < 100 for i in t)
    v = sum(abs(tasks[i]["est"] - tasks[i]["actual"]) for i in t)
    return {"Completed": c, "In Progress": ip, "Pending": total - c - ip, "Health Score": round((c/total)*100 - v, 2)}

def forecast_project_completion(pid):
    t = projects[pid]["tasks"]
    est, actual = sum(tasks[i]["est"] for i in t), sum(tasks[i]["actual"] for i in t)
    if not actual: return "No data"
    ratio = actual / est
    s = datetime.strptime(projects[pid]["start"], "%Y-%m-%d")
    days = (datetime.now() - s).days
    return (s + timedelta(days=int(days / ratio))).strftime("%Y-%m-%d")

def menu():
    while True:
        print("\n=== Project Manager ===")
        print("1. Create Project\n2. Add Team Member\n3. Create Task\n4. Assign Task")
        print("5. Set Dependency\n6. Log Time\n7. Update Progress\n8. View Project Health")
        print("9. Forecast Completion\n0. Exit")

        choice = input("Select option: ")

        try:
            if choice == "1":
                pid = input("Project ID: ")
                name = input("Project Name: ")
                start = input("Start Date (YYYY-MM-DD): ")
                end = input("End Date (YYYY-MM-DD): ")
                priority = input("Priority: ")
                create_project(pid, name, start, end, priority)
                print("Project created.")

            elif choice == "2":
                mid = input("Member ID: ")
                name = input("Name: ")
                role = input("Role: ")
                skills = input("Skills (comma-separated): ").split(",")
                rate = float(input("Hourly Rate: "))
                add_team_member(mid, name, role, skills, rate)
                print("Team member added.")

            elif choice == "3":
                tid = input("Task ID: ")
                pid = input("Project ID: ")
                title = input("Title: ")
                desc = input("Description: ")
                est = float(input("Estimated Hours: "))
                create_task(tid, pid, title, desc, est)
                print("Task created.")

            elif choice == "4":
                tid = input("Task ID: ")
                mid = input("Member ID: ")
                priority = input("Priority Level: ")
                assign_task(tid, mid, priority)
                print("Task assigned.")

            elif choice == "5":
                tid = input("Task ID: ")
                dep = input("Depends on Task ID: ")
                set_task_dependency(tid, dep)
                print("Dependency set.")

            elif choice == "6":
                mid = input("Member ID: ")
                tid = input("Task ID: ")
                hours = float(input("Hours Worked: "))
                date = input("Date (YYYY-MM-DD): ")
                log_time(mid, tid, hours, datetime.strptime(date, "%Y-%m-%d"))
                print("Time logged.")

            elif choice == "7":
                tid = input("Task ID: ")
                pct = int(input("Completion %: "))
                update_task_progress(tid, pct)
                print("Progress updated.")

            elif choice == "8":
                pid = input("Project ID: ")
                print("Project Health:", calculate_project_health(pid))

            elif choice == "9":
                pid = input("Project ID: ")
                print("Forecast Completion:", forecast_project_completion(pid))

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid option.")

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    menu()

