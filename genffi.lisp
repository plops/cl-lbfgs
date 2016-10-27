

(eval-when (:compile-toplevel)
  (ql:quickload :cl-autowrap))

(defpackage :f
  (:use :cl :autowrap))

(in-package :f)

#+nil
(delete-file "lbfgs.x86_64-pc-linux-gnu.spec")

(c-include "lbfgs.h"
	   :spec-path (merge-pathnames "stage/cl-lbfgs/"
				       (user-homedir-pathname))
	   :exclude-arch ("arm-pc-linux-gnu"
			  "i386-unknown-freebsd"
			  "i386-unknown-openbsd"
			  "i686-apple-darwin9"
			  "i686-pc-linux-gnu"
			  "i686-pc-windows-msvc"
			  "x86_64-apple-darwin9"
                                        ;"x86_64-pc-linux-gnu"
			  "x86_64-pc-windows-msvc"
			  "x86_64-unknown-freebsd"
			  "x86_64-unknown-openbsd")
	   :exclude-sources ("/usr/*")
	   :include-definitions ("lbfgs")
	   ;:sysincludes '("/usr/local/include")
	   :trace-c2ffi t )
