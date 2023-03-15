
#ifndef TMPLT_EXPORT_H
#define TMPLT_EXPORT_H

#ifdef TMPLT_STATIC_DEFINE
#  define TMPLT_EXPORT
#  define TMPLT_NO_EXPORT
#else
#  ifndef TMPLT_EXPORT
#    ifdef LibraryTemplate_EXPORTS
        /* We are building this library */
#      define TMPLT_EXPORT __attribute__((visibility("default")))
#    else
        /* We are using this library */
#      define TMPLT_EXPORT __attribute__((visibility("default")))
#    endif
#  endif

#  ifndef TMPLT_NO_EXPORT
#    define TMPLT_NO_EXPORT __attribute__((visibility("hidden")))
#  endif
#endif

#ifndef TMPLT_DEPRECATED
#  define TMPLT_DEPRECATED __attribute__ ((__deprecated__))
#endif

#ifndef TMPLT_DEPRECATED_EXPORT
#  define TMPLT_DEPRECATED_EXPORT TMPLT_EXPORT TMPLT_DEPRECATED
#endif

#ifndef TMPLT_DEPRECATED_NO_EXPORT
#  define TMPLT_DEPRECATED_NO_EXPORT TMPLT_NO_EXPORT TMPLT_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef TMPLT_NO_DEPRECATED
#    define TMPLT_NO_DEPRECATED
#  endif
#endif

#endif /* TMPLT_EXPORT_H */
