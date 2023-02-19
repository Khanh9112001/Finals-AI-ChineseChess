from Const.Const import MATE_VALUE
from Network.Network import Server
from AI.Search import Search
from Log.Logger import Logger
from Const.Const import REPETITION_LOOP_TIMES

s = Server()
s.accept()
logger = Logger("Main")

while True:
    data = s.receive()
    fen = data[0]
    depth = data[1]
    logger.info("receive FEN from client: " + fen + "<----------------------------------")

    searchObj = Search(fen, 3)
    # move = searchObj.search_root()
    move = searchObj.interative_depth_first_search()
    # move = searchObj.search_root_alpha_beta_tt(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_alpha_beta_move_ordering_quiescence_search_TT(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_negamax_alpha_beta_move_ordering_quiescence_search(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_negamax_alpha_beta_move_ordering(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_alpha_beta_move_ordering_TT(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_negamax_alpha_beta(-MATE_VALUE, MATE_VALUE)
    # move = searchObj.search_root_negamax()
    logger.info("the max fixed depth is :" + str(searchObj.maxDepth))
    logger.info(
        "the max highest depth by quiescence search is :" + str(searchObj.position.depthByQuiesc))
    logger.info("the number of searched node is :" + str(searchObj.position.allNode))
    logger.info("send move to client:" + str(move) + "<-----------------------------------")

    # send data back to client
    if move != 0:
        searchObj.position.make_move(move)
        Search.history_heap.append(searchObj.position.zobristLock)
        if len(Search.history_heap) > REPETITION_LOOP_TIMES:
            Search.history_heap.pop(0)
    fen = searchObj.position.to_fen()
    s.send([fen, move])
