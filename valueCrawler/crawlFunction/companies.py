__author__ = 'yazhu'
import json, urllib2, datetime
from util import retry
from valueCrawler.models import Company, SecForm

# Crawl all companies
import logging
logger = logging.getLogger('companyCrawler')


def getAllCompanies():
    offset = 0

    logger.info("crawling companies started!")
    print("crawling companies started! \n")
    while True:
        print("opening url \n")
        data = urlopen_with_retry("http://sec.kimonolabs.com/companies?apikey=iv2stYAlaKITqEJ1CN4fwpSLHSZyF6EH&offset="
                                      + str(offset))
        for sec in data :
            company = Company()
            if sec['name']:
                company.name = sec['name']
            if sec['exchange']:
                company.exchange = sec['exchange']
            if sec['sic_description']:
                company.sicDescription = sec['sic_description']
            company.entityId = sec['entityid']
            company.sicCode = sec['sic_code']
            if sec['symbol']:
                company.symbol = sec['symbol']
            company.save()
            if sec['symbol']:
                forms = urlopen_with_retry("http://sec.kimonolabs.com/companies/" + sec['symbol']
                                           + "/forms?apikey=iv2stYAlaKITqEJ1CN4fwpSLHSZyF6EH")
                for form in forms:
                    if form['name'] == '10-K':
                        companyForms = urlopen_with_retry("http://sec.kimonolabs.com/companies/" + sec['symbol']
                                                         + "/forms/10-k/ann?apikey=iv2stYAlaKITqEJ1CN4fwpSLHSZyF6EH")

                        for companyForm in companyForms:
                            secForm = SecForm()
                            secForm.company = company
                            secForm.year = jsonDataWrapper(companyForm['year'])
                            secForm.period = companyForm['period']
                            secForm.quarter = jsonDataWrapper(companyForm['quarter'])
                            secForm.usdConversionRate = companyForm['usdconversionrate']
                            secForm.periodEndDate = datetime.datetime.strptime(companyForm['periodenddate'], "%m/%d/%Y")
                            secForm.currencyCode = companyForm['currencycode']
                            secForm.changeInCurrentAssets = jsonDataWrapper(companyForm['changeincurrentassets'])
                            secForm.changeInCurrentLiabilities = jsonDataWrapper(companyForm['changeincurrentliabilities'])
                            secForm.changeInInventories = jsonDataWrapper(companyForm['changeininventories'])
                            secForm.dividendsPaid = jsonDataWrapper(companyForm['dividendspaid'])
                            secForm.capitalExpenditures = jsonDataWrapper(companyForm['capitalexpenditures'])
                            secForm.cashFromFinancingActivities = jsonDataWrapper(companyForm['cashfromfinancingactivities'])
                            secForm.cashFromInvestingActivities = jsonDataWrapper(companyForm['cashfrominvestingactivities'])
                            secForm.cashFromOperatingActivities = jsonDataWrapper(companyForm['cashfromoperatingactivities'])
                            secForm.cfDepreciationAmortization = jsonDataWrapper(companyForm['cfdepreciationamortization'])
                            secForm.changeInAccountsReceivable = jsonDataWrapper(companyForm['changeinaccountsreceivable'])
                            secForm.investmentChangesnet = jsonDataWrapper(companyForm['investmentchangesnet'])
                            secForm.netChangeInCash = jsonDataWrapper(companyForm['netchangeincash'])
                            secForm.totalAdjustments = jsonDataWrapper(companyForm['totaladjustments'])
                            secForm.equityEarnings = jsonDataWrapper(companyForm['equityearnings'])
                            secForm.grossProfit = jsonDataWrapper(companyForm['grossprofit'])
                            secForm.interestExpense = jsonDataWrapper(companyForm['interestexpense'])
                            secForm.netIncome = jsonDataWrapper(companyForm['netincome'])
                            secForm.netIncomeApplicableToCommon = jsonDataWrapper(companyForm['netincomeapplicabletocommon'])
                            secForm.researchDevelopmentExpense = jsonDataWrapper(companyForm['researchdevelopmentexpense'])
                            secForm.totalRevenue = jsonDataWrapper(companyForm['totalrevenue'])
                            secForm.sellingGeneralAdministrativeExpenses = jsonDataWrapper(companyForm['sellinggeneraladministrativeexpenses'])
                            secForm.commonStock = jsonDataWrapper(companyForm['commonstock'])
                            secForm.cashAndCashEquivalents = jsonDataWrapper(companyForm['cashandcashequivalents'])
                            secForm.cashEquivalentsAndShortTermInvestments = jsonDataWrapper(companyForm['cashcashequivalentsandshortterminvestments'])
                            secForm.intangibleAssets = jsonDataWrapper(companyForm['intangibleassets'])
                            secForm.goodwill = jsonDataWrapper(companyForm['goodwill'])
                            secForm.inventoriesNet = jsonDataWrapper(companyForm['inventoriesnet'])
                            secForm.minorityInterest = jsonDataWrapper(companyForm['minorityinterest'])
                            secForm.otherAssets = jsonDataWrapper(companyForm['otherassets'])
                            secForm.otherLiabilities = jsonDataWrapper(companyForm['otherliabilities'])
                            secForm.otherEquity = jsonDataWrapper(companyForm['otherequity'])
                            secForm.otherCurrentLiabilities = jsonDataWrapper(companyForm['othercurrentliabilities'])
                            secForm.otherCurrentAssets = jsonDataWrapper(companyForm['othercurrentassets'])
                            secForm.preferredStock = jsonDataWrapper(companyForm['preferredstock'])
                            secForm.propertyPlantEquipmentnet = jsonDataWrapper(companyForm['propertyplantequipmentnet'])
                            secForm.retainedEarnings = jsonDataWrapper(companyForm['retainedearnings'])
                            secForm.totalAssets = jsonDataWrapper(companyForm['totalassets'])
                            secForm.totalCurrentAssets = jsonDataWrapper(companyForm['totalcurrentassets'])
                            secForm.totalCurrentLiabilities = jsonDataWrapper(companyForm['totalcurrentliabilities'])
                            secForm.totalLiabilities = jsonDataWrapper(companyForm['totalliabilities'])
                            secForm.totalLongTermDebt = jsonDataWrapper(companyForm['totallongtermdebt'])
                            secForm.totalReceivablesNet = jsonDataWrapper(companyForm['totalreceivablesnet'])
                            secForm.totalShortTermDebt = jsonDataWrapper(companyForm['totalshorttermdebt'])
                            secForm.totalStockholdersEquity = jsonDataWrapper(companyForm['totalstockholdersequity'])
                            secForm.treasuryStock = jsonDataWrapper(companyForm['treasurystock'])
                            secForm.save()

        length = len(data)

        if length > 0:
            offset += length
            logger.info("finished one call, now offset at " + str(offset))
            print("finished one call, now offset at " + str(offset) + '\n')
        else:
            break


def jsonDataWrapper(field):
    if field:
        if isinstance(field, str):
            try:
                return int(field)
            except Exception:
                return field
    else:
        return None

@retry(Exception, tries=50, delay=3, backoff=2)
def urlopen_with_retry(link):
    return json.load(urllib2.urlopen(link, timeout=20))
