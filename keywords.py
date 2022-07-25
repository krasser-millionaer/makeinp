blocknames = {"autoci", "basis", "casscf", "cipsi", "cim", "cis", "coords", "cpcm", "elprop", "eprnmr", "esd",
              "freq", "geom", "loc", "mcrpa", "md", "mdci", "method", "moinp", "mp2", "mrcc", "mrci", "numgrad", "nbo",
              "output", "paras", "plots", "rel", "rocis", "rr", "scf", "symmetry", "vpt2"}

# 0 -- option parameter
# 1 -- option *params end
# 2 -- string with regular expression
# 3 -- not supported yet


keywords = {
            #%eprnmr block kw's
            ("solver", 0), ("tol", 0), ("maxiter", 0), ("maxdiis", 0), ("levelshift", 0), ("giao_2el", 0),
            ("gtensor", 0), ("dtensor", 0), ("dsoc", 0), ("dss", 0), ("printlevel", 0), ("ori", 0), ("nuclei", 0),
            #%vpt2 block kw's
            ("vpt2", 0), ("avgprop", 0), ("anharmdisp", 0), ("hessiancutoff", 0), ("printlevel", 0), ("minimiseorcaprint", 0),
            #%method block kw's
            ("functional", 0), ("correlation", 0), ("symrelax", 0), ("frozencore", 0), ("angulargrid", 0),
            ("intacc", 0), ("z_tol", 0),
            #%geom block kw's
            ("constraints", 1), ("invertconstraints", 0), ("optimizehydrogens", 0), ("inhess", 0), ("inhessname", 0),
            ("calchess", 0), ("hybrid_hess", 1), ("recalc_hess", 0), ("trust", 0), ("ghostfrags", 1), ("fragments", 1),
            ("gdiismaxeq", 0), ("usegdiis", 0), ("addextrabonds", 0), ("addextrabonds_maxlength", 0), ("addextrabonds_maxdist", 0),
            ("reduceredints", 0), ("constrainfragments", 1), ("connectfragments", 1), ("scan", 1), ("fullscan", 0),
            ("TS_Mode", 1), ("ts_active_atoms", 1), ("ts_active_atoms_factor", 0), ("modify_internal", 1),
            ("potentials", 1), ("printinternalhess", 0), ("maxiter", 0), ("optelement", 0), ("frags", 3), ("relaxfrags", 1),
            ("rigidfrags", 1), ("reconvcharge", 0), ("read_temp_hess", 0), ("hess_internal", 1), ("fragments", 3),
            ("coordsys", 0), ("usesoscf", 0), ("reduceprint", 0), ("optguess", 0),
            #%basis block
            ("basis", 0), ("newgto", 1), ("auxc", 0), ("auxj", 0), ("auxjk", 0), ("auxc", 0), ("newauxcgto", 1), ("aux", 0),
            ("cabs", 0), ("decontractbas", 0), ("decontractauxj", 0), ("decontractauxjk", 0), ("decontractauxc", 0),
            ("decontractcabs", 0), ("decontract", 0), ("autoauxsize", 0), ("autoauxlmax", 0), ("oldautoaux", 0),
            (r"autoaux[fb]\[\d+\]", 2), ("autoauxtightb", 0), ("newauxjgto", 1), ("newauxjkgto", 1), ("gtoname", 0),
            ("gtoauxjname", 0), ("gtoauxjkname", 0), ("gtoauxcname", 0), ("gtocabsname", 0), ("ecp", 0), ("newecp", 1),
            ("delecp", 0), ("pactrimbas", 0), ("pacdtrimauxj", 0), ("pcdtrimauxjk", 0), ("pcdtrimauxc", 0), ("pcdthresh", 0)
}

# ---- To add
# 1) Support for fragments format
# 2) Description for NewGTO (several options, better read from file)
# 3) AddGTO (and likewise auxilliary basis sets) -- complex case
