def product(lst):
	rlst_out = 1
	for i in lst:
		rlst_out *=i		
	return int(rlst_out)

print product(lst)
