
#ifndef LIBRARYTEMPLATE_EXPORT_H
#define LIBRARYTEMPLATE_EXPORT_H

#ifdef LIBRARYTEMPLATE_STATIC_DEFINE
#  define LIBRARYTEMPLATE_EXPORT
#  define LIBRARYTEMPLATE_NO_EXPORT
#else
#  ifndef LIBRARYTEMPLATE_EXPORT
#    ifdef LibraryTemplate_EXPORTS
        /* We are building this library */
#      define LIBRARYTEMPLATE_EXPORT __declspec(dllexport)
#    else
        /* We are using this library */
#      define LIBRARYTEMPLATE_EXPORT __declspec(dllimport)
#    endif
#  endif

#  ifndef LIBRARYTEMPLATE_NO_EXPORT
#    define LIBRARYTEMPLATE_NO_EXPORT 
#  endif
#endif

#ifndef LIBRARYTEMPLATE_DEPRECATED
#  define LIBRARYTEMPLATE_DEPRECATED __declspec(deprecated)
#endif

#ifndef LIBRARYTEMPLATE_DEPRECATED_EXPORT
#  define LIBRARYTEMPLATE_DEPRECATED_EXPORT LIBRARYTEMPLATE_EXPORT LIBRARYTEMPLATE_DEPRECATED
#endif

#ifndef LIBRARYTEMPLATE_DEPRECATED_NO_EXPORT
#  define LIBRARYTEMPLATE_DEPRECATED_NO_EXPORT LIBRARYTEMPLATE_NO_EXPORT LIBRARYTEMPLATE_DEPRECATED
#endif

#if 0 /* DEFINE_NO_DEPRECATED */
#  ifndef LIBRARYTEMPLATE_NO_DEPRECATED
#    define LIBRARYTEMPLATE_NO_DEPRECATED
#  endif
#endif

#endif /* LIBRARYTEMPLATE_EXPORT_H */
