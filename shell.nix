with import <nixpkgs> {};

mkShell {
	  NIX_LD_LIBRARY_PATH = lib.makeLibraryPath [
		      stdenv.cc.cc
				      zlib
					    ];
	    NIX_LD = lib.fileContents "${stdenv.cc}/nix-support/dynamic-linker";
		  buildInputs = [
			python311
			python311Packages.pip
			python311Packages.tkinter						
		  ];
		    shellHook = ''
				    export LD_LIBRARY_PATH=$NIX_LD_LIBRARY_PATH
					  '';
}
