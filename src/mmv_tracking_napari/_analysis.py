
from qtpy.QtWidgets import (QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton,
                            QCheckBox, QHBoxLayout, QGridLayout)

class AnalysisWindow(QWidget):
    """
    A (QWidget) window to run analysis on the data.
    
    Attributes
    ----------
    
    Methods
    -------
    """
    
    def __init__(self):
        """
        Parameters
        ----------
        """
        super().__init__()
        self.setLayout(QVBoxLayout())
        self.setWindowTitle("Analysis")
        
        ### QObjects
        
        # Labels
        label_min_movement = QLabel("Movement Minmum")
        label_min_duration = QLabel("Minimum Track Length")
        label_metric = QLabel("Evaluation metrics:")
                
        # Buttons
        btn_plot = QPushButton("Plot")
        btn_export = QPushButton("Export")
        btn_evaluate_segmentation = QPushButton("Evaluate Segmentation")
        btn_evaluate_tracking = QPushButton("Evaluate Tracking")
        
        # Comboboxes
        combobox_plots = QComboBox()
        combobox_plots.addItems(["speed", "size", "direction", "euclidean distance", "accumulated distance"])
        
        # Checkboxes
        checkbox_speed = QCheckBox("Speed")
        checkbox_size = QCheckBox("Size")
        checkbox_direction = QCheckBox("Direction")
        checkbox_euclidean_distance = QCheckBox("Euclidean distance")
        checkbox_accumulated_distance = QCheckBox("Accumulated distance")
        
        # Line Edits
        lineedit_movement = QLineEdit("")
        lineedit_track_duration = QLineEdit("")
        lineedit_limit_evaluation = QLineEdit("0")
        
        ### Organize objects via widgets
        content = QWidget()
        content.setLayout(QVBoxLayout())
        
        threshhold_grid = QWidget()
        threshhold_grid.setLayout(QGridLayout())
        threshhold_grid.layout().addWidget(label_min_movement, 0, 0)
        threshhold_grid.layout().addWidget(lineedit_movement, 0, 1)
        threshhold_grid.layout().addWidget(label_min_duration, 1, 0)
        threshhold_grid.layout().addWidget(lineedit_track_duration, 1, 1)
        
        content.layout().addWidget(threshhold_grid)
        
        extract_grid = QWidget()
        extract_grid.setLayout(QGridLayout())
        extract_grid.layout().addWidget(label_metric, 0, 0)
        extract_grid.layout().addWidget(combobox_plots, 0, 1)
        extract_grid.layout().addWidget(btn_plot, 0, 2)
        extract_grid.layout().addWidget(checkbox_speed, 1, 0)
        extract_grid.layout().addWidget(checkbox_size, 1, 1)
        extract_grid.layout().addWidget(checkbox_direction, 1, 2)
        extract_grid.layout().addWidget(checkbox_euclidean_distance, 2, 0)
        extract_grid.layout().addWidget(checkbox_accumulated_distance, 2, 1)
        extract_grid.layout().addWidget(btn_export, 2, 2)
        
        content.layout().addWidget(extract_grid)
        content.layout().addWidget(lineedit_limit_evaluation)
        
        evaluation = QWidget()
        evaluation.setLayout(QHBoxLayout())
        evaluation.layout().addWidget(btn_evaluate_segmentation)
        evaluation.layout().addWidget(btn_evaluate_tracking)
        
        content.layout().addWidget(evaluation)
        
        self.layout().addWidget(content)
        
        
        
        
        