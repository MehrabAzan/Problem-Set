def manage_stage_changes(changes):
    stack = []
    cancelID = ""
    for instruction in changes:
        if instruction.startswith("Schedule "):
            scheduleID = instruction.split(" ")
            stack.append(scheduleID[1])
        elif instruction == "Cancel":
            cancelID = stack.pop()
        elif instruction == "Reschedule":
            if cancelID:
                stack.append(cancelID)
    return stack

print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 