# The following has been generated automatically from src/gui/layout/qgslayoutviewtool.h
QgsLayoutViewTool.FlagSnaps = QgsLayoutViewTool.Flag.FlagSnaps
QgsLayoutViewTool.Flags = lambda flags=0: QgsLayoutViewTool.Flag(flags)
try:
    QgsLayoutViewTool.__attribute_docs__ = {'activated': 'Emitted when the tool is activated.\n', 'deactivated': 'Emitted when the tool is deactivated.\n', 'itemFocused': 'Emitted when an ``item`` is "focused" by the tool, i.e. it should become\nthe active item and should have its properties displayed in any designer\nwindows.\n'}
    QgsLayoutViewTool.__virtual_methods__ = ['layoutMoveEvent', 'layoutDoubleClickEvent', 'layoutPressEvent', 'layoutReleaseEvent', 'wheelEvent', 'keyPressEvent', 'keyReleaseEvent', 'activate', 'deactivate', 'ignoredSnapItems']
    QgsLayoutViewTool.__signal_arguments__ = {'itemFocused': ['item: QgsLayoutItem']}
    QgsLayoutViewTool.__group__ = ['layout']
except (NameError, AttributeError):
    pass
