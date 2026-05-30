def format_number(number, decimals=2, thousands_sep=',', decimal_sep='.', prefix='', suffix=''):
    formatted = f"{number:,.{decimals}f}"
    if thousands_sep != ',' or decimal_sep != '.':
        formatted = formatted.replace(',', '__THOU__')
        formatted = formatted.replace('.', decimal_sep)
        formatted = formatted.replace('__THOU__', thousands_sep)
    return f"{prefix}{formatted}{suffix}"

def format_currency(number, symbol='$', decimals=2):
    return format_number(number, decimals=decimals, prefix=symbol)

def format_percentage(number, decimals=1):
    return format_number(number, decimals=decimals, suffix='%')

def format_compact(number):
    abs_num = abs(number)
    sign = '-' if number < 0 else ''
    if abs_num >= 1_000_000_000:
        return f"{sign}{abs_num / 1_000_000_000:.1f}B"
    elif abs_num >= 1_000_000:
        return f"{sign}{abs_num / 1_000_000:.1f}M"
    elif abs_num >= 1_000:
        return f"{sign}{abs_num / 1_000:.1f}K"
    return f"{sign}{abs_num}"