

def getNameFiles():
    """Returns a dictionary of the subcategories and their corresponding model files. 
    Key: Name of subcategory
    Value: Touple that holds bottleneck file[0] and class indices[1]"""
    
    subCategories = {
    "Deep Fryer": deepFryerFiles(),
    "Deli Bar": deliBarFiles(),
    "Dishwasher": dishwahserFiles(),
    "Exhaust Systems": exhaustSystemsFiles(),
    "Grills": grillsFiles(),
    "Hot Beverage Machine": hotBeverageMachineFiles(),
    "Hot Holding Units": hotHoldingUnitFiles(),
    "Iced Beverage Machine": icedBeverageMachineFiles(),
    "Ovens": ovensFiles(),
    "Reach In Freezer": reachInFreezerFiles(),
    "Smallware A": smallwareAFiles(),
    "Smallware B": smallwareBFiles(),
    "Smallware C": smallwareCFiles(),
    "Smallware D": smallwareDFiles(),
    "Smallware E": smallwareEFiles(),
    "Smallware F": smallwareFFiles(),
    "Smallware G": smallwareGFiles(),
    "Sugar": sugarFiles(),
    "Under Counter Cooler": underCounterCoolerFiles()
    
    }
    
    return subCategories

def deepFryerFiles():
    files = getFile("deepfryergraph.pp", "deepfryerlabels.txt", "Model Files")
    return (files[0], files[1])

def deliBarFiles():
    files = getFile("delibargraph.pp", "delibarlabels.txt", "Model Files")
    return (files[0], files[1])

def dishwahserFiles():
    files = getFile("dishwashergraph.pp", "dishwasherlabels.txt", "Model Files")
    return (files[0], files[1])

def exhaustSystemsFiles():
    files = getFile("exhaustsystemsgraph.pp", "exhaustsystemslabels.txt", "Model Files")
    return (files[0], files[1])

def grillsFiles():
    files = getFile("grillsgraph.pp", "grillslabels.txt", "Model Files")
    return (files[0], files[1])

def hotBeverageMachineFiles():
    files = getFile("hotbeveragemachinegraph.pp", "hotbeveragemachinelabels.txt", "Model Files")
    return (files[0], files[1])

def hotHoldingUnitFiles():
    files = getFile("hotholdingunitsgraph.pp", "hotholdingunitslabels.txt", "Model Files")
    return (files[0], files[1])

def icedBeverageMachineFiles():
    files = getFile("icedbeveragemachinegraph.pp", "icedbeveragemachinelabels.txt", "Model Files")
    return (files[0], files[1])

def ovensFiles():
    files = getFile("ovensgraph.pp", "ovenslabels.txt", "Model Files")
    return (files[0], files[1])

def reachInFreezerFiles():
    files = getFile("reachinfreezergraph.pp", "reachinfreezerlabels.txt", "Model Files")
    return (files[0], files[1])


def smallwareAFiles():
    files = getFile("SmallwareAgraph.pp", "SmallwareAlabels.txt", "Model Files")
    return (files[0], files[1])

def smallwareBFiles():
    files = getFile("SmallwareBgraph.pp", "SmallwareBlabels.txt", "Model Files")
    return (files[0], files[1])


def smallwareCFiles():
    files = getFile("SmallwareCgraph.pp", "SmallwareClabels.txt", "Model Files")
    return (files[0], files[1])

def smallwareDFiles():
    files = getFile("SmallwareDgraph.pp", "SmallwareDlabels.txt", "Model Files")
    return (files[0], files[1])

def smallwareEFiles():
    files = getFile("SmallwareEgraph.pp", "SmallwareElabels.txt", "Model Files")
    return (files[0], files[1])


def smallwareFFiles():
    files = getFile("SmallwareFgraph.pp", "SmallwareFlabels.txt", "Model Files")
    return (files[0], files[1])

def smallwareGFiles():
    files = getFile("SmallwareGgraph.pp", "SmallwareGlabels.txt", "Model Files")
    return (files[0], files[1])


def sugarFiles():
    files = getFile("sugargraph.pp", "sugarlabels.txt", "Model Files")
    return (files[0], files[1])

def underCounterCoolerFiles():
    files = getFile("undercountercoolergraph.pp", "undercountercoolerlabels.txt", "Model Files")
    return (files[0], files[1])


def getFile(bottleneckFileName, classFileName, folderName):
    return (r"{folder}\\{bottleneck}".format(folder = folderName, bottleneck = bottleneckFileName), r"{folder}\\{classIndices}".format(folder = folderName, classIndices = classFileName))












