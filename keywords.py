blocknames = {"autoci", "basis", "casscf", "cipsi", "cim", "cis", "coords", "cpcm", "elprop", "eprnmr", "esd",
              "freq", "geom", "loc", "mcrpa", "md", "mdci", "method", "mp2", "mrcc", "mrci", "numgrad", "nbo",
              "output", "paras", "plots", "rel", "rocis", "rr", "scf", "symmetry", "vpt2"}

# 0 -- option parameter
# 1 -- option *params end
# 2 -- strings containing " or '
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
            ("constraints", 1), ("invertconstraints", 0), ("optimizehydrogens", 0), ("inhess", 0), ("inhessname", 2),
            ("calchess", 0), ("hybrid_hess", 1), ("recalc_hess", 0), ("trust", 0), ("ghostfrags", 1), ("fragments", 1),
            ("gdiismaxeq", 0), ("usegdiis", 0), ("addextrabonds", 0), ("addextrabonds_maxlength", 0), ("addextrabonds_maxdist", 0),
            ("reduceredints", 0), ("constrainfragments", 1), ("connectfragments", 1), ("scan", 1), ("fullscan", 0),
            ("TS_Mode", 1), ("ts_active_atoms", 1), ("ts_active_atoms_factor", 0), ("modify_internal", 1),
            ("potentials", 1), ("printinternalhess", 0), ("maxiter", 0), ("optelement", 0), ("frags", 3), ("relaxfrags", 1),
            ("rigidfrags", 1), ("reconvcharge", 0), ("read_temp_hess", 0), ("hess_internal", 1), ("fragments", 3),
            ("coordsys", 0), ("usesoscf", 0), ("reduceprint", 0), ("optguess", 0)
}