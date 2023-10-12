from fastapi import FastAPI, Body

app = FastAPI(
    title="Project Management API",
    description="An API for managing projects",
    docs_url='/'
)

"""
{
    "name": "The Songs of Adelaide & Abullah",
    "category": "Poetry",
    "main_category": "Publishing",
    "goal": 1000.0
},
{
    "name": "Greeting From Earth: ZGAC Arts Capsule For ET",
    "category": "Narrative Film",
    "main_category": "Film & Video",
    "goal": 30000.0
},
{
    "category": "Narrative Film",
    "goal": 45000.0,
    "main_category": "Film & Video",
    "name": "Where is Hank?"
}
"""

projects_list = []

def get_project_id(projects_list):
    """
    Return the Project ID information based on the list of projects
    present in our in-memory database
    """
    if projects_list:
        return projects_list[-1]['project_id'] + 1
    return 1

# @app.get('/')
# def hello():
#     return {"message": "Welcome to Python API Training with FastAPI"}

@app.get('/projects')
def fetch_all_projects():
    """
    Display all projects
    """
    return projects_list

@app.post("/projects")
def add_project(new_project=Body()):
    """
    Add a project
    """
    new_project["project_id"] = get_project_id(projects_list)
    projects_list.append(new_project)

@app.put("/projects/{project_id}")
def update_book(project_id: int, data=Body()):
    print(project_id)
    for project in projects_list:
        if project["project_id"] == project_id:
            project["name"] = data["name"]
            project["category"] = data["category"]
            project["goal"] = data["goal"]
            project["main_category"] = data["main_category"]
            return {}
    else:
        return {'message': f"Project with ID: {project_id} is not found"}