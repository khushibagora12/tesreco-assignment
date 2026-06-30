## 6. shallow vs deep copy

import copy

intern_projects = ["ML", "web dev", "devops"]
print("initially: ", intern_projects)

shallow_copy = intern_projects
deep_copy = copy.deepcopy(intern_projects)
print("shallow: ", shallow_copy)
print("deep: ", deep_copy)

deep_copy.append("app dev")
print("after changing deep: ", deep_copy)
print("after making changes in depp, original: ", intern_projects)

shallow_copy.append("app dev")
print("after changing shallow: ", shallow_copy)
print("after making changes in shallow, original: ", intern_projects)


