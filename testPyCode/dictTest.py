import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from  import taskManegerClassProjectManager
from taskClass import Task

pjm = ProjectManager()

#! pj1定義、task1,2追加
pjm.add_project("pj1")
pjm.add_task("pj1",Task("task011","2023/11/21"))
pjm.add_task("pj1",Task("task012","2023/11/22"))

#! pj2定義、task1,2,3追加
pjm.add_project("pj2")
pjm.add_task("pj2",Task("task021","2023/11/23"))
pjm.add_task("pj2",Task("task022","2023/11/24"))
pjm.add_task("pj2",Task("task023","2023/11/25"))

pjm.display_projects()
print(list(pjm.projects.keys())[1])