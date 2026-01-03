# module_parsing

Read and parse all the Manim modules and extract documentation from them.

### Type Aliases

### *class* AliasInfo

```default
dict[str, str]
```

Dictionary with a definition key containing the definition of
a `TypeAlias` as a string, and optionally a doc key containing
the documentation for that alias, if it exists.

### *class* AliasCategoryDict

```default
dict[str, [`AliasInfo`](#manim.utils.docbuild.module_parsing.AliasInfo)]
```

Dictionary which holds an [`AliasInfo`](#manim.utils.docbuild.module_parsing.AliasInfo) for every alias name in a same
category.

### *class* ModuleLevelAliasDict

```default
dict[str, [`AliasCategoryDict`](#manim.utils.docbuild.module_parsing.AliasCategoryDict)]
```

Dictionary containing every `TypeAlias` defined in a module,
classified by category in different [`AliasCategoryDict`](#manim.utils.docbuild.module_parsing.AliasCategoryDict) objects.

### *class* ModuleTypeVarDict

```default
dict[str, str]
```

Dictionary containing every `TypeVar` defined in a module.

### *class* AliasDocsDict

```default
dict[str, [`ModuleLevelAliasDict`](#manim.utils.docbuild.module_parsing.ModuleLevelAliasDict)]
```

Dictionary which, for every module in Manim, contains documentation
about their module-level attributes which are explicitly defined as
`TypeAlias`, separating them from the rest of attributes.

### *class* DataDict

```default
dict[str, list[str]]
```

Type for a dictionary which, for every module, contains a list with
the names of all their DOCUMENTED module-level attributes (identified
by Sphinx via the `data` role, hence the name) which are NOT
explicitly defined as `TypeAlias`.

### *class* TypeVarDict

```default
dict[str, [`ModuleTypeVarDict`](#manim.utils.docbuild.module_parsing.ModuleTypeVarDict)]
```

A dictionary mapping module names to dictionaries of `TypeVar` objects.

### Functions

### parse_module_attributes()

Read all files, generate Abstract Syntax Trees from them, and
extract useful information about the type aliases defined in the
files: the category they belong to, their definition and their
description, separating them from the “regular” module attributes.

* **Returns:**
  * **ALIAS_DOCS_DICT** ([`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict)) – A dictionary containing the information from all the type
    aliases in Manim. See [`AliasDocsDict`](#manim.utils.docbuild.module_parsing.AliasDocsDict) for more information.
  * **DATA_DICT** ([`DataDict`](#manim.utils.docbuild.module_parsing.DataDict)) – A dictionary containing the names of all DOCUMENTED
    module-level attributes which are not a `TypeAlias`.
  * **TYPEVAR_DICT** ([`TypeVarDict`](#manim.utils.docbuild.module_parsing.TypeVarDict)) – A dictionary containing the definitions of `TypeVar` objects,
    organized by modules.
* **Return type:**
  tuple[[*AliasDocsDict*](#manim.utils.docbuild.module_parsing.AliasDocsDict), [*DataDict*](#manim.utils.docbuild.module_parsing.DataDict), [*TypeVarDict*](#manim.utils.docbuild.module_parsing.TypeVarDict)]
