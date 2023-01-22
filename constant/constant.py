

class Constant:
    connSuccessfully = "Connected Successfully"
    connCantConn = "Can't connect to MySQL"
    connClose = "MySQL connection is closed"
    startConnDB = "Start Connect Database"
    executeFailed = "Execute Failed"
    readFailed = "Select Faild"
    exceptionWording = "Exception : "
    sqlWording = "SQL : "
    paramsWording = "Params : "
    respWording = "Response : "
    startFuction = "------------------------ Start %s ------------------------"
    endFunction = "------------------------ End %s ------------------------"
    errDB = "errDB"
    actionSuccessfully = "%s Successfully"
    actionFailed = "%s Failed"
    idIsNotFound = "id Is Not Found"

    #name funtion
    toDoList = "toDoList"
    insertToDo = "insertToDo"
    editToDo = "editToDo"
    deleteToDo = "deleteToDo"
    findToDoList = "findToDoList"

    #resp code
    successfullyCode = "00"
    failedCode = "01"
    incorrectDateFormatCode = "errValid01"
    finishdtMoreTodayCode = "errValid02"
    idIsNoneCode = "errValid03"
    leastOneDataCode = "errValid04"

    #resp msg
    incorrectDateFormatMsg = "Incorrect data format, should be YYYY-MM-DD HH:mm:ss"
    finishdtMoreTodayMsg = "Effective finish_dt must be more than current datetime."
    idIsNoneMsg = "id Is None"
    leastOneDataMsg = "[content,finish_dt,status] At least 1 data is required."

    #format
    formatDT = "%Y-%m-%d %H:%M:%S"

    #action database
    actionSelect = "Select"
    actionInsert = "Insert"
    actionUpdate = "Update"
    actionDelete = "Delete"