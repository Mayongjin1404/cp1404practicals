from project import Project

def load_projects(filename):
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        return [Project.from_string(line.strip()) for line in file]

def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStartDate\tPriority\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.completion}\n")

def display_projects(projects):
    incomplete_projects = sorted([p for p in projects if not p.is_complete()], key=lambda p: p.priority)
    completed_projects = sorted([p for p in projects if p.is_complete()], key=lambda p: p.priority)

    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)

    print("\nCompleted Projects:")
    for project in completed_projects:
        print(project)

def filter_projects_by_date(projects, date):
    filtered_projects = sorted([p for p in projects if p.start_date > date], key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)

def add_new_project(projects):
    name = input("Enter project name: ")
    start_date = input("Enter project start date (YYYY-MM-DD): ")
    priority = int(input("Enter project priority: "))
    completion = int(input("Enter project completion %: "))
    project = Project(name, start_date, priority, completion)
    projects.append(project)

def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project}")

    choice = int(input("Choose a project to update: "))
    project = projects[choice - 1]

    new_priority = input("Enter new priority (blank to skip): ")
    new_completion = input("Enter new completion % (blank to skip): ")

    if new_priority:
        project.priority = int(new_priority)
    if new_completion:
        project.completion = int(new_completion)

def main():
    projects = []

    while True:
        print("""
        1. Load projects
        2. Save projects
        3. Display projects
        4. Filter projects by date
        5. Add new project
        6. Update project
        7. Quit
        """)
        choice = input("Choose an option: ")

        if choice == '1':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == '2':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == '3':
            display_projects(projects)
        elif choice == '4':
            date = input("Enter date (YYYY-MM-DD) to filter by: ")
            filter_projects_by_date(projects, date)
        elif choice == '5':
            add_new_project(projects)
        elif choice == '6':
            update_project(projects)
        elif choice == '7':
            break

if __name__ == "__main__":
    main()
