import Test_Case

SERVER = '10.0.0.76'
PORT = 5555
test_connection = Test_Case.Test_Server_Connection(SERVER, PORT)
test_connection.connection()

test_suggestion = Test_Case.Test_Suggestion(0,0,0,0,(0,0,0),'No accusation', 'No suggestion','0.0.0.0',5555)
test_suggestion.sugg()

test_accusation = Test_Case.Test_Accusation(0,0,0,0,(0,0,0),'No accusation', 'No suggestion','0.0.0.0',5555)
test_accusation.acc()