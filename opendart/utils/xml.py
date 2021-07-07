from xml.etree.ElementTree import fromstring


def check_status(xml_text: str) -> None:
    root = fromstring(xml_text)
    status = root.findtext('status')
    message = root.findtext('message')

    if status != '000':
        raise Exception(f"{status}: {message}")

def check_validation():
    '''
    재무제표에 대한 FinancialStatement.find 알고리즘의 유효성 검사
    '''
    pass