import xml.etree.ElementTree as ET
from Const.const import CHESSMAN


class XMLHandler:
    PATH = "./Database/"

    @staticmethod
    def search_database(fen_list, fen_input):
        """
        :param fen_list:
        :param fen_input: fen input
        :return: fen output response
        """
        for Fense in fen_list:
            for subelem in Fense.findall('inputFense'):
                if subelem.text == fen_input:
                    print("This case existed")
                    # return Fense.find('outputFense').text
                    return True

    @staticmethod
    def load_file(fen):
        count_piece = 0
        for i in range(len(fen)):
            if fen[i] in CHESSMAN:
                count_piece += 1
        print(count_piece)
        path = XMLHandler.PATH + str(count_piece) + '.xml'
        try:
            tree = ET.parse(path)
            fen_list = tree.getroot()
            return [fen_list, path, tree]
        except:
            return [0, path, '']

    @staticmethod
    def insert(fen_input, fen_output):
        exist_inputfen = False
        [FenseList, path, tree] = XMLHandler.load_file(fen_input)
        if FenseList == 0:
            print('FIlE NONE')
            FenseList = ET.Element("FenseList")
            FenseList.tail = "\n"
            FenseList.text = "\n"
            attrib = {}
            Fense = FenseList.makeelement('Fense', attrib)
            Fense.tail = "\n"
            Fense.text = "\n\t\t"
            new_fen_input = ET.SubElement(Fense, 'inputFense')
            new_fen_input.tail = "\n\t\t"
            new_fen_input.text = fen_input
            new_fen_output = ET.SubElement(Fense, 'outputFense')
            new_fen_output.tail = "\n"
            new_fen_output.text = fen_output
            FenseList.append(Fense)
            tree = ET.ElementTree(FenseList)
            tree.write(path)
            print('Add this case in database')
        else:
            if XMLHandler.search_database(FenseList, fen_input):
                exist_inputfen = True
            print(exist_inputfen)
            if not exist_inputfen:
                attrib = {}
                Fense = FenseList.makeelement('Fense', attrib)
                Fense.tail = "\n"
                Fense.text = "\n\t\t"
                new_fen_input = ET.SubElement(Fense, 'inputFense')
                new_fen_input.tail = "\n\t\t"
                new_fen_input.text = fen_input
                new_fen_output = ET.SubElement(Fense, 'outputFense')
                new_fen_output.tail = "\n"
                new_fen_output.text = fen_output
                FenseList.append(Fense)
                tree.write(path)
                print('Add this case in database')
