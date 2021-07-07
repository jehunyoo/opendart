"""
Configuration for OpenDART
"""

# URLs
BASE_URL = "https://opendart.fss.or.kr/api/"

# Corporation Information
CORP_CODE_XML = "corpCode.xml"

# Financial Information
SINGLE_FS_XML = "fnlttSinglAcntAll.xml"
SINGLE_FS_JSON = "fnlttSinglAcntAll.json"

# Request Keys
QUATER_REPORT_KEYS = {1: "11013", 2: "11012", 3: "11014", 4: "11011"}
FS_DIV_KEYS = {1: "CFS", 0: "OFS"}

# Response Keys
TERM_KEYS = {0: "thstrm_amount", 1: "frmtrm_amount", 2: "bfefrmtrm_amount"}

STATEMENT_KEYS = {
    "BS": "재무상태표",
    "IS": "손익계산서",
    "CIS" : "포괄손익계산서",
    "CF": "현금흐름표",
    "SCE" : "자본변동표"
}
INVERSE_STATEMENT_KEYS = {value: key for key, value in STATEMENT_KEYS.items()}

# Default Location
CORP_CODE_LOCATION = "temp/CORPCODE.xml"


# IDs of items of financial statement
ITEM_ID = {
    # Statement of Financial Position (재무상태표)
    '유동자산': 'ifrs-full_CurrentAssets',
    '현금및현금성자산': 'ifrs-full_CashAndCashEquivalents',
    '단기금융상품': 'dart_ShortTermDepositsNotClassifiedAsCashEquivalents',
    '유동당기손익-공정가치측정지정금융자산': 'ifrs-full_CurrentFinancialAssetsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition',
    '파생상품자산': 'dart_CurrentDerivativeAsset',
    '매출채권': 'dart_ShortTermTradeReceivable',
    '기타유동금융자산': 'ifrs-full_OtherCurrentFinancialAssets',
    '재고자산': 'ifrs-full_Inventories',
    '매각예정자산': 'ifrs-full_NoncurrentAssetsOrDisposalGroupsClassifiedAsHeldForSaleOrAsHeldForDistributionToOwners',
    '기타유동자산': 'dart_OtherCurrentAssets',
    #--------------------------------------------------
    '비유동자산': 'ifrs-full_NoncurrentAssets',
    '장기금융상품': 'dart_LongTermDepositsNotClassifiedAsCashEquivalents',
    '당기손익-공정가치측정금융자산': 'ifrs-full_NoncurrentFinancialAssetsAtFairValueThroughProfitOrLossDesignatedUponInitialRecognition',
    '기타포괄손익-공정가치측정금융자산': 'ifrs-full_NoncurrentFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncome',
    '관계기업및공동기업투자': 'ifrs-full_InvestmentsInAssociates',
    '기타비유동금융자산': 'ifrs-full_OtherNoncurrentFinancialAssets',
    '유형자산': 'ifrs-full_PropertyPlantAndEquipment',
    '무형자산': 'dart_OtherIntangibleAssetsGross',
    '투자부동산': 'ifrs-full_InvestmentProperty',
    '사용권자산': 'ifrs-full_RightofuseAssets',
    '기타비유동자산': 'dart_OtherNonCurrentAssets',
    '이연법인세자산': 'ifrs-full_DeferredTaxAssets',
    '자산총계': 'ifrs-full_Assets',
    #--------------------------------------------------
    '유동부채': 'ifrs-full_CurrentLiabilities',
    '매입채무및기타채무': 'ifrs-full_TradeAndOtherCurrentPayables',
    '단기차입금': 'ifrs-full_ShorttermBorrowings',
    '기타유동금융부채': 'ifrs-full_OtherCurrentFinancialLiabilities',
    '미지급법인세': 'dart_PaymentsOfIncomeTaxesPayable',
    '충당부채': 'ifrs-full_CurrentProvisions',
    '파생상품부채': 'dart_CurrentDerivativeLiabilities',
    '단기리스부채': 'ifrs-full_CurrentLeaseLiabilities',
    '기타유동부채': 'dart_OtherCurrentLiabilities',
    #--------------------------------------------------
    '비유동부채': 'ifrs-full_NoncurrentLiabilities',
    '비유동매입채무및기타채무': 'dart_LongTermTradeAndOtherNonCurrentPayables',
    '장기차입금': 'dart_LongTermBorrowingsGross',
    '비유동충당부채': 'ifrs-full_NoncurrentProvisions',
    '장기리스부채': 'ifrs-full_NoncurrentLeaseLiabilities',
    '순확정급여부채': 'dart_PostemploymentBenefitObligations',
    '기타장기종업원급여부채': 'ifrs-full_NoncurrentProvisionsForEmployeeBenefits',
    '비유동파생상품부채': 'dart_NonCurrentDerivativeLiabilities',
    '이연법인세부채': 'ifrs-full_DeferredTaxLiabilities',
    '기타비유동금융부채': 'ifrs-full_OtherNoncurrentFinancialLiabilities',
    '기타비유동부채': 'dart_OtherNonCurrentLiabilities',
    '부채총계': 'ifrs-full_Liabilities',
    #--------------------------------------------------
    '지배기업소유주지분': 'ifrs-full_EquityAttributableToOwnersOfParent',
    '자본금': 'ifrs-full_IssuedCapital',
    '자본잉여금': 'dart_CapitalSurplus',
    '자본조정': 'dart_ElementsOfOtherStockholdersEquity',
    '기타포괄손익누계액': 'dart_OtherComprehensiveIncomeLossAccumulatedAmount',
    '이익잉여금(결손금)': 'ifrs-full_RetainedEarnings',
    '비지배지분': 'ifrs-full_NoncontrollingInterests',
    '자본총계': 'ifrs-full_Equity',
    '부채와자본총계': 'ifrs-full_EquityAndLiabilities',
    # Income Statement (손익계산서)
    '매출': 'ifrs-full_Revenue',
    '매출원가': 'ifrs-full_CostOfSales',
    '매출총이익': 'ifrs-full_GrossProfit',
    '영업수익': 'ifrs-full_GrossProfit',
    '영업비용': 'dart_TotalSellingGeneralAdministrativeExpenses',
    '영업이익': 'dart_OperatingIncomeLoss',
    '기타수익': 'dart_OtherGains',
    '기타비용': 'dart_OtherLosses',
    '금융수익': 'ifrs-full_FinanceIncome',
    '이자수익': 'dart_InterestIncomeFinanceIncome',
    '기타금융수익': 'dart_OtherFinancialIncome',
    '금융비용': 'ifrs-full_FinanceCosts',
    '지분법이익': 'ifrs-full_GainsArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost',
    '지분법손실': 'ifrs-full_LossesArisingFromDerecognitionOfFinancialAssetsMeasuredAtAmortisedCost',
    '법인세비용차감전순이익(손실)': 'ifrs-full_ProfitLossBeforeTax',
    '법인세비용': 'ifrs-full_IncomeTaxExpenseContinuingOperations',
    '당기순이익': 'ifrs-full_ProfitLoss',
    '지배기업소유주지분': 'ifrs-full_ProfitLossAttributableToOwnersOfParent',
    '비지배지분': 'ifrs-full_ProfitLossAttributableToNoncontrollingInterests',
    '기본주당이익': 'ifrs-full_BasicEarningsLossPerShare',
    '희석주당이익': 'ifrs-full_DilutedEarningsLossPerShare',
    # Statement of Comprehensive Income (포괄손익계산서)
    '기타포괄손익': 'ifrs-full_OtherComprehensiveIncome',
    '후속적으로당기손익으로재분류될수없는항목': 'dart_OtherComprehensiveIncomeThatWillNotBeReclassifiedToProfitOrLossNetOfTax',
    '순확정급여부채의재측정요소': 'dart_OtherComprehensiveIncomeNetOfTaxGainsLossesOnRemeasurementsOfDefinedBenefitPlans',
    '기타포괄손익-공정가치측정지분상품평가손익': 'ifrs-full_OtherComprehensiveIncomeNetOfTaxGainsLossesFromInvestmentsInEquityInstruments',
    '재평가잉여금': 'ifrs-full_OtherComprehensiveIncomeNetOfTaxGainsLossesOnRevaluation',
    '후속적으로당기손익으로재분류될수있는항목': 'dart_OtherComprehensiveIncomeThatWillBeReclassifiedToProfitOrLossNetOfTax',
    '기타포괄손익-공정가치측정채무상품평가이익': 'ifrs-full_GainsLossesOnFinancialAssetsMeasuredAtFairValueThroughOtherComprehensiveIncomeNetOfTax',
    '부의지분법자본변동': 'dart_ShareOfOtherComprehensiveIncomeOfAssociatesAndJointVenturesAccountedForUsingEquityMethodThatWillBeReclassifiedToProfitOrLossNetOfTax',
    '해외사업환산이익': 'ifrs-full_GainsLossesOnExchangeDifferencesOnTranslationNetOfTax',
    '총포괄손익': 'ifrs-full_ComprehensiveIncome',
    '지배기업소유주지분': 'ifrs-full_ComprehensiveIncomeAttributableToOwnersOfParent',
    '비지배지분': 'ifrs-full_ComprehensiveIncomeAttributableToNoncontrollingInterests',
    # Statement of Cash Flows (현금흐름표)
    '영업활동현금흐름': 'ifrs-full_CashFlowsFromUsedInOperatingActivities',
    '영업으로부터창출된현금흐름': 'dart_AdjustmentsForAssetsLiabilitiesOfOperatingActivities',
    '이자의수취': 'ifrs-full_InterestReceivedClassifiedAsOperatingActivities',
    '이자의지급': 'ifrs-full_InterestPaidClassifiedAsOperatingActivities',
    '배당금수입': 'ifrs-full_DividendsReceivedClassifiedAsOperatingActivities',
    '법인세납부': 'ifrs-full_IncomeTaxesPaidRefundClassifiedAsOperatingActivities',
    '투자활동현금흐름': 'ifrs-full_CashFlowsFromUsedInInvestingActivities',
    '단기금융상품의증감': 'dart_ProceedsFromSalesOfShortTermFinancialInstruments',
    '장기금융상품의증감': 'dart_ProceedsFromSalesOfLongTermFinancialInstruments',
    '유형자산의취득': 'ifrs-full_PurchaseOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
    '유형자산의처분': 'ifrs-full_ProceedsFromSalesOfPropertyPlantAndEquipmentClassifiedAsInvestingActivities',
    '투자부동산의처분': 'dart_ProceedsFromSalesOfInvestmentProperty',
    '무형자산의취득': 'ifrs-full_PurchaseOfIntangibleAssetsClassifiedAsInvestingActivities',
    '무형자산의처분': 'ifrs-full_ProceedsFromSalesOfIntangibleAssetsClassifiedAsInvestingActivities',
    '당기손익-공정가치측정금융자산의취득': 'dart_PurchaseOfFairValueFinancialAsset',
    '당기손익-공정가치측정금융자산의처분': 'dart_ProceedsFromSalesOfFairValueFinancialAsset',
    '기타포괄손익-공정가치측정금융자산의취득': 'ifrs-full_OtherCashPaymentsToAcquireEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities',
    '기타포괄손익-공정가치측정금융자산의처분': 'ifrs-full_OtherCashReceiptsFromSalesOfEquityOrDebtInstrumentsOfOtherEntitiesClassifiedAsInvestingActivities',
    '관계기업및공동기업투자의취득': 'dart_PurchaseOfInvestmentsInAssociates',
    '관계기업및공동기업투자의처분': 'dart_ProceedsFromSalesOfInvestmentsInAssociates',
    '종속기업취득및연결범위변동으로인한순현금흐름': 'ifrs-full_CashFlowsUsedInObtainingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities',
    '종속기업처분및연결범위변동으로인한순현금흐름': 'ifrs-full_CashFlowsFromLosingControlOfSubsidiariesOrOtherBusinessesClassifiedAsInvestingActivities',
    '기타금융자산의증가': 'dart_PurchaseOfOtherFinancialAssets',
    '기타금융자산의감소': 'dart_ProceedsFromSalesOfOtherFinancialAssets',
    '기타비유동금융자산의증가': 'dart_PurchaseOfOtherNonCurrentFinancialAssets',
    '기타비유동금융자산의감소': 'dart_ProceedsFromSalesOfOtherNonCurrentFinancialAssets',
    '기타투자활동으로인한현금흐름': 'ifrs-full_OtherInflowsOutflowsOfCashClassifiedAsInvestingActivities',
    '재무활동현금흐름': 'ifrs-full_CashFlowsFromUsedInFinancingActivities',
    '단기차입금의차입': 'dart_ProceedsFromShortTermBorrowings',
    '단기차입금의상환': 'dart_RepaymentsOfShortTermBorrowings',
    '장기차입금의차입': 'dart_ProceedsFromLongTermBorrowings',
    '장기차입금의상환': 'dart_RepaymentsOfLongTermBorrowings',
    '리스부채의상환': 'ifrs-full_PaymentsOfFinanceLeaseLiabilitiesClassifiedAsFinancingActivities',
    '유상증자': 'ifrs-full_ProceedsFromIssuingShares',
    '주식선택권의행사': 'dart_ProceedsFromExerciseOfShareOptions',
    '배당금지급': 'ifrs-full_DividendsPaidClassifiedAsFinancingActivities',
    '자기주식의취득': 'dart_AcquisitionOfTreasuryShares',
    '비지배지분의취득': 'dart_PaymentForConsolidatedCapitalTransactions',
    '출자금의중간분배': 'dart_PaymentForStockRedemption',
    '종속회사추가출자(비지배주주)': 'ifrs-full_ProceedsFromChangesInOwnershipInterestsInSubsidiaries',
    '기타재무활동으로인한현금유출액': 'ifrs-full_OtherInflowsOutflowsOfCashClassifiedAsFinancingActivities',
    '현금및현금성자산에대한환율변동효과': 'ifrs-full_EffectOfExchangeRateChangesOnCashAndCashEquivalents',
    '현금및현금성자산의순증가(감소)': 'ifrs-full_IncreaseDecreaseInCashAndCashEquivalents',
    '기초현금및현금성자산': 'dart_CashAndCashEquivalentsAtBeginningOfPeriodCf',
    '기말현금및현금성자산': 'dart_CashAndCashEquivalentsAtEndOfPeriodCf',
    # Statement of Changes in Equity (자본변동표)
}