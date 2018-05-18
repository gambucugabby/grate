import grate

#Gender Sort
print grate.ProcFiles(['CommaDelimited'], 1)
#Birthday Sort
print grate.ProcFiles(['PipeDelimited'], 2)
#Last Name Sort
print grate.ProcFiles(['SpaceDelimited'], 3)
#mutliple arrys for the heck of it
print grate.ProcFiles(['CommaDelimited','PipeDelimited','SpaceDelimited'], 1)
#Return sort w/o input
print grate.ProcFiles([], 1)
