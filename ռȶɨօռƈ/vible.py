'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'
def vible(
    amount,
    last='B'):
    if amount is None:
        amount = 0
    else:
        amount = int(amount)
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(amount) < 1024.0:
            return "%3.1f%s%s" % (
                amount,
                unit,
                last)
        amount /= 1024.0
    return "%.1f%s%s" % (
        amount,
        'Yi',
        last)
'🍟==============================『🍗 ʏօʊȶʊɮɛʟɨ 🍰』==============================🍟'