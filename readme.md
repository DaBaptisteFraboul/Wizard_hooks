#   Fire - Promo 2023 - Wizard Hooks

###  TODO LIST :DOCUMENT:

- Faire un hook qui génère un fbx de manière automatique lors de 
l'export de modeling => Faire un export de LOD1 avec le smooth mesh desactivé.
L'export doit se faire dans un nouveau nom d'export, par exemple :

``EXPORT :
    - LOD1
    - LOD2
    - LOD3
    - TEXTURING``

- Changer la manière dont guerilla importe les texture, il faut que chaque materiaux
de l'asset texture ait son propre node de ``materialoverride`` dans GuerillaRender.
Actuellement Wizard ne génère qu'un  ``materialoverride`` car il n'attend qu'un seul jeu 
de texture depuis Substance Painter. Faire un ``materialoverride`` par jeu de texture.
Peut-être réfléchir à un moyen de l'intégrer directement dans Wizard car cela risque de poser le même problème que
que pour le renommage des RenderGraphs