def dose(needs):
    output = []
    vita = []
    inj = []
    for attribute in needs:
        if 0 <= attribute < 250:
            if attribute % 10 == 0:
                vita.append(int(attribute / 10))
                inj.append(0)
            else:
                vita.append(int(attribute // 10 + 1))
                inj.append(int(vita[-1] * 10 - attribute))
        elif attribute >= 250 or sum(attribute)>500:
            return(("No medicine given"))
    output = list(zip(vita, inj))
    return output



