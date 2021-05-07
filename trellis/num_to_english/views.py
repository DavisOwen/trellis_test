from rest_framework.decorators import api_view, throttle_classes, permission_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework import permissions

class CustomUserThrottle(UserRateThrottle):
    rate = '100/day'

group_of_three = {
    0: '',
    1: ' thousand',
    2: ' million',
    3: ' billion',
}

singles = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

teens = {
    0: 'ten',
    1: 'eleven',
    2: 'twelve',
    3: 'thirteen',
    4: 'fourteen',
    5: 'fifteen',
    6: 'sixteen',
    7: 'seventeen',
    8: 'eighteen',
    9: 'nineteen',
}

doubles = {
    2: 'twenty',
    3: 'thirty',
    4: 'fourty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

@api_view(['GET'])
@throttle_classes([CustomUserThrottle])
@permission_classes([permissions.IsAuthenticated])
def num_to_english(request):
    num = request.GET.get('number')
    if not num:
        return Response({'status': 'fail', 'error': 'incorrect payload format'})
    try:
        int_num = int(num)
    except ValueError:
        return Response({'status': 'fail', 'error': 'incorrect number supplied'})
    if int_num >= 10**12 or int_num < 0:
        return Response({'status': 'fail', 'error': 'only numbers between 0 and 10^12 supported'})
    result = ''
    if int_num == 0:
        result = 'zero'
    else:
        n = len(num)
        # keeping track on if we are a "teen" number
        teen = False
        for i in range(n):
            curr_num = int(num[i])
            # find out how many groups of 3's we can
            # break number into
            three_groups = ((n - 1) - i) // 3
            # find remainder after groups of 3
            three_mod = ((n - 1) - i) % 3
            space = i > 0 and not (not teen and curr_num == 0) and result != ''
            # hundreds
            if three_mod == 2:
                if space:
                    result += ' '
                result += (singles[curr_num] + ' hundred') if curr_num > 0 else ''
                three_mod = 3
            # tens
            elif three_mod == 1:
                if curr_num > 1:
                    if space:
                        result += ' '
                    result += doubles[curr_num]
                elif curr_num == 1:
                    teen = True
            # single digits
            elif three_mod == 0:
                if space:
                    result += ' '
                if teen:
                    result += teens[curr_num]
                    teen = False
                else:
                    result += singles[curr_num]
                # append group of three (thousand, million, etc.)
                result += group_of_three[three_groups]
    return Response({'status': 'ok', 'num_in_english': result})
