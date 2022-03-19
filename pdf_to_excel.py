import datetime

import pandas
import tabula


def main():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi,')  # Press Ctrl+F8 to toggle the breakpoint.
    pdf = tabula.read_pdf("N&O-293.pdf", pages="120-192")

    columns = ['Code', 'Freq', 'Date', 'UTC', 'Day', 'Details', 'Mode', 'Contributor']
    df = pandas.DataFrame(columns=columns)
    for i in range(1, len(pdf)):
        pdf[i].columns = columns
        df = pandas.concat([df, pdf[i]], ignore_index=True)
        # df = df.append(pdf[i], ignore_index=True)

    # df.apply(lambda x: pandas.Series(x.dropna().values))
    df = df.dropna()

    df['Date'] = df['Date'].apply(lambda d: datetime.datetime.strptime(d + ' 2022', '%d-%m %Y').strftime('%Y-%m-%d'))
    df['UTC'] = df['UTC'].apply(lambda t: datetime.datetime.strptime(str(int(t)), '%H%M').strftime('%H:%M'))
    # date = datetime.datetime.strptime('3-2' + ' 2022', '%d-%m %Y').strftime('%Y-%m-%d')
    # time = datetime.datetime.strptime('700', '%H%M').strftime('%H:%M')
    # print(date)
    # print(time)

    df.to_excel("logs.xlsx")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
