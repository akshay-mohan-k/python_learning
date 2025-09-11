def http_status(status):
    match status:
        case 200:
            return "ok"
        case 400:
            return "not ok"
       