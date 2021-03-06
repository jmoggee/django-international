# -*- coding: utf-8 -*-
"""
This file is part of django-international.
Copyright (c) 2012 Monwara LLC.
All rights reserved.

Licensed under BSD license. See LICENSE file for more details.
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _


babel = None
print("WARNING, language names will not be available")

__all__ = ['countries_raw', 'countries', 'currencies', 'languages',
           'languages_native', 'languages_english', 'Country']

"""Countries and currencies

Country data includes 2- and 3-letter ISO codes, continents, and full country
names. Currency data includes 3-letter ISO code and full currency name.

Country fixtures are provided but they are not in the form of initial data,
since we might want to edit the country list at some point, depending on our
needs.

"""

countries_raw = (
    ("AS", "AF", "AFG", 4, _("Afghanistan, Islamic Republic of")),
    ("EU", "AL", "ALB", 8, _("Albania, Republic of")),
    ("AN", "AQ", "ATA", 10, _("Antarctica (the territory South of 60 deg S)")),
    ("AF", "DZ", "DZA", 12, _("Algeria, People's Democratic Republic of")),
    ("OC", "AS", "ASM", 16, _("American Samoa")),
    ("EU", "AD", "AND", 20, _("Andorra, Principality of")),
    ("AF", "AO", "AGO", 24, _("Angola, Republic of")),
    ("NA", "AG", "ATG", 28, _("Antigua and Barbuda")),
    ("AS", "AZ", "AZE", 31, _("Azerbaijan, Republic of")),
    ("SA", "AR", "ARG", 32, _("Argentina, Argentine Republic")),
    ("OC", "AU", "AUS", 36, _("Australia, Commonwealth of")),
    ("EU", "AT", "AUT", 40, _("Austria, Republic of")),
    ("NA", "BS", "BHS", 44, _("Bahamas, Commonwealth of the")),
    ("AS", "BH", "BHR", 48, _("Bahrain, Kingdom of")),
    ("AS", "BD", "BGD", 50, _("Bangladesh, People's Republic of")),
    ("AS", "AM", "ARM", 51, _("Armenia, Republic of")),
    ("NA", "BB", "BRB", 52, _("Barbados")),
    ("EU", "BE", "BEL", 56, _("Belgium, Kingdom of")),
    ("NA", "BM", "BMU", 60, _("Bermuda")),
    ("AS", "BT", "BTN", 64, _("Bhutan, Kingdom of")),
    ("SA", "BO", "BOL", 68, _("Bolivia, Republic of")),
    ("EU", "BA", "BIH", 70, _("Bosnia and Herzegovina")),
    ("AF", "BW", "BWA", 72, _("Botswana, Republic of")),
    ("AN", "BV", "BVT", 74, _("Bouvet Island (Bouvetoya)")),
    ("SA", "BR", "BRA", 76, _("Brazil, Federative Republic of")),
    ("NA", "BZ", "BLZ", 84, _("Belize")),
    ("AS", "IO", "IOT", 86, _("British Indian Ocean Territory (Chagos Archipelago)")),
    ("OC", "SB", "SLB", 90, _("Solomon Islands")),
    ("NA", "VG", "VGB", 92, _("British Virgin Islands")),
    ("AS", "BN", "BRN", 96, _("Brunei Darussalam")),
    ("EU", "BG", "BGR", 100, _("Bulgaria, Republic of")),
    ("AS", "MM", "MMR", 104, _("Myanmar, Union of")),
    ("AF", "BI", "BDI", 108, _("Burundi, Republic of")),
    ("EU", "BY", "BLR", 112, _("Belarus, Republic of")),
    ("AS", "KH", "KHM", 116, _("Cambodia, Kingdom of")),
    ("AF", "CM", "CMR", 120, _("Cameroon, Republic of")),
    ("NA", "CA", "CAN", 124, _("Canada")),
    ("AF", "CV", "CPV", 132, _("Cape Verde, Republic of")),
    ("NA", "KY", "CYM", 136, _("Cayman Islands")),
    ("AF", "CF", "CAF", 140, _("Central African Republic")),
    ("AS", "LK", "LKA", 144, _("Sri Lanka, Democratic Socialist Republic of")),
    ("AF", "TD", "TCD", 148, _("Chad, Republic of")),
    ("SA", "CL", "CHL", 152, _("Chile, Republic of")),
    ("AS", "CN", "CHN", 156, _("China, People's Republic of")),
    ("AS", "TW", "TWN", 158, _("Taiwan")),
    ("AS", "CX", "CXR", 162, _("Christmas Island")),
    ("AS", "CC", "CCK", 166, _("Cocos (Keeling) Islands")),
    ("SA", "CO", "COL", 170, _("Colombia, Republic of")),
    ("AF", "KM", "COM", 174, _("Comoros, Union of the")),
    ("AF", "YT", "MYT", 175, _("Mayotte")),
    ("AF", "CG", "COG", 178, _("Congo, Republic of the")),
    ("AF", "CD", "COD", 180, _("Congo, Democratic Republic of the")),
    ("OC", "CK", "COK", 184, _("Cook Islands")),
    ("NA", "CR", "CRI", 188, _("Costa Rica, Republic of")),
    ("EU", "HR", "HRV", 191, _("Croatia, Republic of")),
    ("NA", "CU", "CUB", 192, _("Cuba, Republic of")),
    ("EU", "CY", "CYP", 196, _("Cyprus, Republic of")),
    ("EU", "CZ", "CZE", 203, _("Czech Republic")),
    ("AF", "BJ", "BEN", 204, _("Benin, Republic of")),
    ("EU", "DK", "DNK", 208, _("Denmark, Kingdom of")),
    ("NA", "DM", "DMA", 212, _("Dominica, Commonwealth of")),
    ("NA", "DO", "DOM", 214, _("Dominican Republic")),
    ("SA", "EC", "ECU", 218, _("Ecuador, Republic of")),
    ("NA", "SV", "SLV", 222, _("El Salvador, Republic of")),
    ("AF", "GQ", "GNQ", 226, _("Equatorial Guinea, Republic of")),
    ("AF", "ET", "ETH", 231, _("Ethiopia, Federal Democratic Republic of")),
    ("AF", "ER", "ERI", 232, _("Eritrea, State of")),
    ("EU", "EE", "EST", 233, _("Estonia, Republic of")),
    ("EU", "FO", "FRO", 234, _("Faroe Islands")),
    ("SA", "FK", "FLK", 238, _("Falkland Islands (Malvinas)")),
    ("AN", "GS", "SGS", 239, _("South Georgia and the South Sandwich Islands")),
    ("OC", "FJ", "FJI", 242, _("Fiji, Republic of the Fiji Islands")),
    ("EU", "FI", "FIN", 246, _("Finland, Republic of")),
    ("EU", "AX", "ALA", 248, _("Åland Islands")),
    ("EU", "FR", "FRA", 250, _("France, French Republic")),
    ("SA", "GF", "GUF", 254, _("French Guiana")),
    ("OC", "PF", "PYF", 258, _("French Polynesia")),
    ("AN", "TF", "ATF", 260, _("French Southern Territories")),
    ("AF", "DJ", "DJI", 262, _("Djibouti, Republic of")),
    ("AF", "GA", "GAB", 266, _("Gabon, Gabonese Republic")),
    ("AS", "GE", "GEO", 268, _("Georgia")),
    ("AF", "GM", "GMB", 270, _("Gambia, Republic of the")),
    ("AS", "PS", "PSE", 275, _("Palestinian Territory, Occupied")),
    ("EU", "DE", "DEU", 276, _("Germany, Federal Republic of")),
    ("AF", "GH", "GHA", 288, _("Ghana, Republic of")),
    ("EU", "GI", "GIB", 292, _("Gibraltar")),
    ("OC", "KI", "KIR", 296, _("Kiribati, Republic of")),
    ("EU", "GR", "GRC", 300, _("Greece, Hellenic Republic")),
    ("NA", "GL", "GRL", 304, _("Greenland")),
    ("NA", "GD", "GRD", 308, _("Grenada")),
    ("NA", "GP", "GLP", 312, _("Guadeloupe")),
    ("OC", "GU", "GUM", 316, _("Guam")),
    ("NA", "GT", "GTM", 320, _("Guatemala, Republic of")),
    ("AF", "GN", "GIN", 324, _("Guinea, Republic of")),
    ("SA", "GY", "GUY", 328, _("Guyana, Co-operative Republic of")),
    ("NA", "HT", "HTI", 332, _("Haiti, Republic of")),
    ("AN", "HM", "HMD", 334, _("Heard Island and McDonald Islands")),
    ("EU", "VA", "VAT", 336, _("Holy See (Vatican City State)")),
    ("NA", "HN", "HND", 340, _("Honduras, Republic of")),
    ("AS", "HK", "HKG", 344, _("Hong Kong, Special Administrative Region of China")),
    ("EU", "HU", "HUN", 348, _("Hungary, Republic of")),
    ("EU", "IS", "ISL", 352, _("Iceland, Republic of")),
    ("AS", "IN", "IND", 356, _("India, Republic of")),
    ("AS", "ID", "IDN", 360, _("Indonesia, Republic of")),
    ("AS", "IR", "IRN", 364, _("Iran, Islamic Republic of")),
    ("AS", "IQ", "IRQ", 368, _("Iraq, Republic of")),
    ("EU", "IE", "IRL", 372, _("Ireland")),
    ("AS", "IL", "ISR", 376, _("Israel, State of")),
    ("EU", "IT", "ITA", 380, _("Italy, Italian Republic")),
    ("AF", "CI", "CIV", 384, _("Cote d'Ivoire, Republic of")),
    ("NA", "JM", "JAM", 388, _("Jamaica")),
    ("AS", "JP", "JPN", 392, _("Japan")),
    ("AS", "KZ", "KAZ", 398, _("Kazakhstan, Republic of")),
    ("AS", "JO", "JOR", 400, _("Jordan, Hashemite Kingdom of")),
    ("AF", "KE", "KEN", 404, _("Kenya, Republic of")),
    ("AS", "KP", "PRK", 408, _("Korea, Democratic People's Republic of")),
    ("AS", "KR", "KOR", 410, _("Korea, Republic of")),
    ("AS", "KW", "KWT", 414, _("Kuwait, State of")),
    ("AS", "KG", "KGZ", 417, _("Kyrgyz Republic")),
    ("AS", "LA", "LAO", 418, _("Lao People's Democratic Republic")),
    ("AS", "LB", "LBN", 422, _("Lebanon, Lebanese Republic")),
    ("AF", "LS", "LSO", 426, _("Lesotho, Kingdom of")),
    ("EU", "LV", "LVA", 428, _("Latvia, Republic of")),
    ("AF", "LR", "LBR", 430, _("Liberia, Republic of")),
    ("AF", "LY", "LBY", 434, _("Libyan Arab Jamahiriya")),
    ("EU", "LI", "LIE", 438, _("Liechtenstein, Principality of")),
    ("EU", "LT", "LTU", 440, _("Lithuania, Republic of")),
    ("EU", "LU", "LUX", 442, _("Luxembourg, Grand Duchy of")),
    ("AS", "MO", "MAC", 446, _("Macao, Special Administrative Region of China")),
    ("AF", "MG", "MDG", 450, _("Madagascar, Republic of")),
    ("AF", "MW", "MWI", 454, _("Malawi, Republic of")),
    ("AS", "MY", "MYS", 458, _("Malaysia")),
    ("AS", "MV", "MDV", 462, _("Maldives, Republic of")),
    ("AF", "ML", "MLI", 466, _("Mali, Republic of")),
    ("EU", "MT", "MLT", 470, _("Malta, Republic of")),
    ("NA", "MQ", "MTQ", 474, _("Martinique")),
    ("AF", "MR", "MRT", 478, _("Mauritania, Islamic Republic of")),
    ("AF", "MU", "MUS", 480, _("Mauritius, Republic of")),
    ("NA", "MX", "MEX", 484, _("Mexico, United Mexican States")),
    ("EU", "MC", "MCO", 492, _("Monaco, Principality of")),
    ("AS", "MN", "MNG", 496, _("Mongolia")),
    ("EU", "MD", "MDA", 498, _("Moldova, Republic of")),
    ("EU", "ME", "MNE", 499, _("Montenegro, Republic of")),
    ("NA", "MS", "MSR", 500, _("Montserrat")),
    ("AF", "MA", "MAR", 504, _("Morocco, Kingdom of")),
    ("AF", "MZ", "MOZ", 508, _("Mozambique, Republic of")),
    ("AS", "OM", "OMN", 512, _("Oman, Sultanate of")),
    ("AF", "NA", "NAM", 516, _("Namibia, Republic of")),
    ("OC", "NR", "NRU", 520, _("Nauru, Republic of")),
    ("AS", "NP", "NPL", 524, _("Nepal, State of")),
    ("EU", "NL", "NLD", 528, _("Netherlands, Kingdom of the")),
    ("NA", "AN", "ANT", 530, _("Netherlands Antilles")),
    ("NA", "CW", "CUW", 531, _("Curaçao")),
    ("NA", "AW", "ABW", 533, _("Aruba")),
    ("NA", "SX", "SXM", 534, _("Sint Maarten (Netherlands)")),
    ("NA", "BQ", "BES", 535, _("Bonaire, Sint Eustatius and Saba")),
    ("OC", "NC", "NCL", 540, _("New Caledonia")),
    ("OC", "VU", "VUT", 548, _("Vanuatu, Republic of")),
    ("OC", "NZ", "NZL", 554, _("New Zealand")),
    ("NA", "NI", "NIC", 558, _("Nicaragua, Republic of")),
    ("AF", "NE", "NER", 562, _("Niger, Republic of")),
    ("AF", "NG", "NGA", 566, _("Nigeria, Federal Republic of")),
    ("OC", "NU", "NIU", 570, _("Niue")),
    ("OC", "NF", "NFK", 574, _("Norfolk Island")),
    ("EU", "NO", "NOR", 578, _("Norway, Kingdom of")),
    ("OC", "MP", "MNP", 580, _("Northern Mariana Islands, Commonwealth of the")),
    ("NA", "UM", "UMI", 581, _("United States Minor Outlying Islands")),
    ("OC", "FM", "FSM", 583, _("Micronesia, Federated States of")),
    ("OC", "MH", "MHL", 584, _("Marshall Islands, Republic of the")),
    ("OC", "PW", "PLW", 585, _("Palau, Republic of")),
    ("AS", "PK", "PAK", 586, _("Pakistan, Islamic Republic of")),
    ("NA", "PA", "PAN", 591, _("Panama, Republic of")),
    ("OC", "PG", "PNG", 598, _("Papua New Guinea, Independent State of")),
    ("SA", "PY", "PRY", 600, _("Paraguay, Republic of")),
    ("SA", "PE", "PER", 604, _("Peru, Republic of")),
    ("AS", "PH", "PHL", 608, _("Philippines, Republic of the")),
    ("OC", "PN", "PCN", 612, _("Pitcairn Islands")),
    ("EU", "PL", "POL", 616, _("Poland, Republic of")),
    ("EU", "PT", "PRT", 620, _("Portugal, Portuguese Republic")),
    ("AF", "GW", "GNB", 624, _("Guinea-Bissau, Republic of")),
    ("AS", "TL", "TLS", 626, _("Timor-Leste, Democratic Republic of")),
    ("NA", "PR", "PRI", 630, _("Puerto Rico, Commonwealth of")),
    ("AS", "QA", "QAT", 634, _("Qatar, State of")),
    ("AF", "RE", "REU", 638, _("Reunion")),
    ("EU", "RO", "ROU", 642, _("Romania")),
    ("EU", "RU", "RUS", 643, _("Russian Federation")),
    ("AF", "RW", "RWA", 646, _("Rwanda, Republic of")),
    ("NA", "BL", "BLM", 652, _("Saint Barthelemy")),
    ("AF", "SH", "SHN", 654, _("Saint Helena")),
    ("NA", "KN", "KNA", 659, _("Saint Kitts and Nevis, Federation of")),
    ("NA", "AI", "AIA", 660, _("Anguilla")),
    ("NA", "LC", "LCA", 662, _("Saint Lucia")),
    ("NA", "MF", "MAF", 663, _("Saint Martin")),
    ("NA", "PM", "SPM", 666, _("Saint Pierre and Miquelon")),
    ("NA", "VC", "VCT", 670, _("Saint Vincent and the Grenadines")),
    ("EU", "SM", "SMR", 674, _("San Marino, Republic of")),
    ("AF", "ST", "STP", 678, _("Sao Tome and Principe, Democratic Republic of")),
    ("AS", "SA", "SAU", 682, _("Saudi Arabia, Kingdom of")),
    ("AF", "SN", "SEN", 686, _("Senegal, Republic of")),
    ("EU", "RS", "SRB", 688, _("Serbia, Republic of")),
    ("AF", "SC", "SYC", 690, _("Seychelles, Republic of")),
    ("AF", "SL", "SLE", 694, _("Sierra Leone, Republic of")),
    ("AS", "SG", "SGP", 702, _("Singapore, Republic of")),
    ("EU", "SK", "SVK", 703, _("Slovakia (Slovak Republic)")),
    ("AS", "VN", "VNM", 704, _("Vietnam, Socialist Republic of")),
    ("EU", "SI", "SVN", 705, _("Slovenia, Republic of")),
    ("AF", "SO", "SOM", 706, _("Somalia, Somali Republic")),
    ("AF", "ZA", "ZAF", 710, _("South Africa, Republic of")),
    ("AF", "ZW", "ZWE", 716, _("Zimbabwe, Republic of")),
    ("EU", "ES", "ESP", 724, _("Spain, Kingdom of")),
    ("AF", "SS", "SSD", 728, _("South Sudan")),
    ("AF", "EH", "ESH", 732, _("Western Sahara")),
    ("AF", "SD", "SDN", 736, _("Sudan, Republic of")),
    ("SA", "SR", "SUR", 740, _("Suriname, Republic of")),
    ("EU", "SJ", "SJM", 744, _("Svalbard & Jan Mayen Islands")),
    ("AF", "SZ", "SWZ", 748, _("Swaziland, Kingdom of")),
    ("EU", "SE", "SWE", 752, _("Sweden, Kingdom of")),
    ("EU", "CH", "CHE", 756, _("Switzerland, Swiss Confederation")),
    ("AS", "SY", "SYR", 760, _("Syrian Arab Republic")),
    ("AS", "TJ", "TJK", 762, _("Tajikistan, Republic of")),
    ("AS", "TH", "THA", 764, _("Thailand, Kingdom of")),
    ("AF", "TG", "TGO", 768, _("Togo, Togolese Republic")),
    ("OC", "TK", "TKL", 772, _("Tokelau")),
    ("OC", "TO", "TON", 776, _("Tonga, Kingdom of")),
    ("NA", "TT", "TTO", 780, _("Trinidad and Tobago, Republic of")),
    ("AS", "AE", "ARE", 784, _("United Arab Emirates")),
    ("AF", "TN", "TUN", 788, _("Tunisia, Tunisian Republic")),
    ("EU", "TR", "TUR", 792, _("Turkey, Republic of")),
    ("AS", "TM", "TKM", 795, _("Turkmenistan")),
    ("NA", "TC", "TCA", 796, _("Turks and Caicos Islands")),
    ("OC", "TV", "TUV", 798, _("Tuvalu")),
    ("AF", "UG", "UGA", 800, _("Uganda, Republic of")),
    ("EU", "UA", "UKR", 804, _("Ukraine")),
    ("EU", "MK", "MKD", 807, _("Macedonia, The Former Yugoslav Republic of")),
    ("AF", "EG", "EGY", 818, _("Egypt, Arab Republic of")),
    ("EU", "GB", "GBR", 826, _("United Kingdom")),
    ("EU", "GG", "GGY", 831, _("Guernsey, Bailiwick of")),
    ("EU", "JE", "JEY", 832, _("Jersey, Bailiwick of")),
    ("EU", "IM", "IMN", 833, _("Isle of Man")),
    ("AF", "TZ", "TZA", 834, _("Tanzania, United Republic of")),
    ("NA", "US", "USA", 840, _("United States")),
    ("NA", "VI", "VIR", 850, _("United States Virgin Islands")),
    ("AF", "BF", "BFA", 854, _("Burkina Faso")),
    ("SA", "UY", "URY", 858, _("Uruguay, Eastern Republic of")),
    ("AS", "UZ", "UZB", 860, _("Uzbekistan, Republic of")),
    ("SA", "VE", "VEN", 862, _("Venezuela, Bolivarian Republic of")),
    ("OC", "WF", "WLF", 876, _("Wallis and Futuna")),
    ("OC", "WS", "WSM", 882, _("Samoa, Independent State of")),
    ("AS", "YE", "YEM", 887, _("Yemen")),
    ("AF", "ZM", "ZMB", 894, _("Zambia, Republic of")),
    ("OC", "XX", None, None, _("Disputed Territory")),
    ("AS", "XE", None, None, _("Iraq-Saudi Arabia Neutral Zone")),
    ("AS", "XD", None, None, _("United Nations Neutral Zone")),
    ("AS", "XS", None, None, _("Spratly Islands")),
)

countries = [
    (c[1], c[4].partition(',')[0].partition('(')[0].strip())
    for c in countries_raw
]

continents = (
    ('AF', _('Africa')),
    ('AN', _('Antarctica')),
    ('AS', _('Asia')),
    ('EU', _('Europe')),
    ('NA', _('North America')),
    ('OC', _('Oceania')),
    ('SA', _('South America')),
)

currencies = (
    ('USD', _('USD - United States Dollar')),
    ('EUR', _('EUR - Euro Members')),
    ('JPY', _('JPY - Japan Yen')),
    ('GBP', _('GBP - United Kingdom Pound')),
    ('CHF', _('CHF - Switzerland Franc')),
    ('AED', _('AED - United Arab Emirates Dirham')),
    ('AFN', _('AFN - Afghanistan Afghani')),
    ('ALL', _('ALL - Albania Lek')),
    ('AMD', _('AMD - Armenia Dram')),
    ('ANG', _('ANG - Netherlands Antilles Guilder')),
    ('AOA', _('AOA - Angola Kwanza')),
    ('ARS', _('ARS - Argentina Peso')),
    ('AUD', _('AUD - Australia Dollar')),
    ('AWG', _('AWG - Aruba Guilder')),
    ('AZN', _('AZN - Azerbaijan New Manat')),
    ('BAM', _('BAM - Bosnia and Herzegovina Convertible Marka')),
    ('BBD', _('BBD - Barbados Dollar')),
    ('BDT', _('BDT - Bangladesh Taka')),
    ('BGN', _('BGN - Bulgaria Lev')),
    ('BHD', _('BHD - Bahrain Dinar')),
    ('BIF', _('BIF - Burundi Franc')),
    ('BMD', _('BMD - Bermuda Dollar')),
    ('BND', _('BND - Brunei Darussalam Dollar')),
    ('BOB', _('BOB - Bolivia Boliviano')),
    ('BRL', _('BRL - Brazil Real')),
    ('BSD', _('BSD - Bahamas Dollar')),
    ('BTN', _('BTN - Bhutan Ngultrum')),
    ('BWP', _('BWP - Botswana Pula')),
    ('BYR', _('BYR - Belarus Ruble')),
    ('BZD', _('BZD - Belize Dollar')),
    ('CAD', _('CAD - Canada Dollar')),
    ('CDF', _('CDF - Congo/Kinshasa Franc')),
    ('CLP', _('CLP - Chile Peso')),
    ('CNY', _('CNY - China Yuan Renminbi')),
    ('COP', _('COP - Colombia Peso')),
    ('CRC', _('CRC - Costa Rica Colon')),
    ('CUC', _('CUC - Cuba Convertible Peso')),
    ('CUP', _('CUP - Cuba Peso')),
    ('CVE', _('CVE - Cape Verde Escudo')),
    ('CZK', _('CZK - Czech Republic Koruna')),
    ('DJF', _('DJF - Djibouti Franc')),
    ('DKK', _('DKK - Denmark Krone')),
    ('DOP', _('DOP - Dominican Republic Peso')),
    ('DZD', _('DZD - Algeria Dinar')),
    ('EGP', _('EGP - Egypt Pound')),
    ('ERN', _('ERN - Eritrea Nakfa')),
    ('ETB', _('ETB - Ethiopia Birr')),
    ('FJD', _('FJD - Fiji Dollar')),
    ('FKP', _('FKP - Falkland Islands (Malvinas) Pound')),
    ('GEL', _('GEL - Georgia Lari')),
    ('GGP', _('GGP - Guernsey Pound')),
    ('GHS', _('GHS - Ghana Cedi')),
    ('GIP', _('GIP - Gibraltar Pound')),
    ('GMD', _('GMD - Gambia Dalasi')),
    ('GNF', _('GNF - Guinea Franc')),
    ('GTQ', _('GTQ - Guatemala Quetzal')),
    ('GYD', _('GYD - Guyana Dollar')),
    ('HKD', _('HKD - Hong Kong Dollar')),
    ('HNL', _('HNL - Honduras Lempira')),
    ('HRK', _('HRK - Croatia Kuna')),
    ('HTG', _('HTG - Haiti Gourde')),
    ('HUF', _('HUF - Hungary Forint')),
    ('IDR', _('IDR - Indonesia Rupiah')),
    ('ILS', _('ILS - Israel Shekel')),
    ('IMP', _('IMP - Isle of Man Pound')),
    ('INR', _('INR - India Rupee')),
    ('IQD', _('IQD - Iraq Dinar')),
    ('IRR', _('IRR - Iran Rial')),
    ('ISK', _('ISK - Iceland Krona')),
    ('JEP', _('JEP - Jersey Pound')),
    ('JMD', _('JMD - Jamaica Dollar')),
    ('JOD', _('JOD - Jordan Dinar')),
    ('KES', _('KES - Kenya Shilling')),
    ('KGS', _('KGS - Kyrgyzstan Som')),
    ('KHR', _('KHR - Cambodia Riel')),
    ('KMF', _('KMF - Comoros Franc')),
    ('KPW', _('KPW - Korea (North) Won')),
    ('KRW', _('KRW - Korea (South) Won')),
    ('KWD', _('KWD - Kuwait Dinar')),
    ('KYD', _('KYD - Cayman Islands Dollar')),
    ('KZT', _('KZT - Kazakhstan Tenge')),
    ('LAK', _('LAK - Laos Kip')),
    ('LBP', _('LBP - Lebanon Pound')),
    ('LKR', _('LKR - Sri Lanka Rupee')),
    ('LRD', _('LRD - Liberia Dollar')),
    ('LSL', _('LSL - Lesotho Loti')),
    ('LTL', _('LTL - Lithuania Litas')),
    ('LVL', _('LVL - Latvia Lat')),
    ('LYD', _('LYD - Libya Dinar')),
    ('MAD', _('MAD - Morocco Dirham')),
    ('MDL', _('MDL - Moldova Le')),
    ('MGA', _('MGA - Madagascar Ariary')),
    ('MKD', _('MKD - Macedonia Denar')),
    ('MMK', _('MMK - Myanmar (Burma) Kyat')),
    ('MNT', _('MNT - Mongolia Tughrik')),
    ('MOP', _('MOP - Macau Pataca')),
    ('MRO', _('MRO - Mauritania Ouguiya')),
    ('MUR', _('MUR - Mauritius Rupee')),
    ('MVR', _('MVR - Maldives (Maldive Islands) Rufiyaa')),
    ('MWK', _('MWK - Malawi Kwacha')),
    ('MXN', _('MXN - Mexico Peso')),
    ('MYR', _('MYR - Malaysia Ringgit')),
    ('MZN', _('MZN - Mozambique Metical')),
    ('NAD', _('NAD - Namibia Dollar')),
    ('NGN', _('NGN - Nigeria Naira')),
    ('NIO', _('NIO - Nicaragua Cordoba')),
    ('NOK', _('NOK - Norway Krone')),
    ('NPR', _('NPR - Nepal Rupee')),
    ('NZD', _('NZD - New Zealand Dollar')),
    ('OMR', _('OMR - Oman Rial')),
    ('PAB', _('PAB - Panama Balboa')),
    ('PEN', _('PEN - Peru Nuevo Sol')),
    ('PGK', _('PGK - Papua New Guinea Kina')),
    ('PHP', _('PHP - Philippines Peso')),
    ('PKR', _('PKR - Pakistan Rupee')),
    ('PLN', _('PLN - Poland Zloty')),
    ('PYG', _('PYG - Paraguay Guarani')),
    ('QAR', _('QAR - Qatar Riyal')),
    ('RON', _('RON - Romania New Le')),
    ('RSD', _('RSD - Serbia Dinar')),
    ('RUB', _('RUB - Russia Ruble')),
    ('RWF', _('RWF - Rwanda Franc')),
    ('SAR', _('SAR - Saudi Arabia Riyal')),
    ('SBD', _('SBD - Solomon Islands Dollar')),
    ('SCR', _('SCR - Seychelles Rupee')),
    ('SDG', _('SDG - Sudan Pound')),
    ('SEK', _('SEK - Sweden Krona')),
    ('SGD', _('SGD - Singapore Dollar')),
    ('SHP', _('SHP - Saint Helena Pound')),
    ('SLL', _('SLL - Sierra Leone Leone')),
    ('SOS', _('SOS - Somalia Shilling')),
    ('SPL', _('SPL - Seborga Luigino')),
    ('SRD', _('SRD - Suriname Dollar')),
    ('STD', _('STD - São Tomé and Príncipe Dobra')),
    ('SVC', _('SVC - El Salvador Colon')),
    ('SYP', _('SYP - Syria Pound')),
    ('SZL', _('SZL - Swaziland Lilangeni')),
    ('THB', _('THB - Thailand Baht')),
    ('TJS', _('TJS - Tajikistan Somoni')),
    ('TMT', _('TMT - Turkmenistan Manat')),
    ('TND', _('TND - Tunisia Dinar')),
    ('TOP', _("TOP - Tonga Pa'anga")),
    ('TRY', _('TRY - Turkey Lira')),
    ('TTD', _('TTD - Trinidad and Tobago Dollar')),
    ('TVD', _('TVD - Tuvalu Dollar')),
    ('TWD', _('TWD - Taiwan New Dollar')),
    ('TZS', _('TZS - Tanzania Shilling')),
    ('UAH', _('UAH - Ukraine Hryvna')),
    ('UGX', _('UGX - Uganda Shilling')),
    ('UYU', _('UYU - Uruguay Peso')),
    ('UZS', _('UZS - Uzbekistan Som')),
    ('VEF', _('VEF - Venezuela Bolivar')),
    ('VND', _('VND - Viet Nam Dong')),
    ('VUV', _('VUV - Vanuatu Vat')),
    ('WST', _('WST - Samoa Tala')),
    ('XAF', _('XAF - Communauté Financière Africaine (BEAC) CFA Franc BEAC')),
    ('XCD', _('XCD - East Caribbean Dollar')),
    ('XDR', _('XDR - International Monetary Fund (IMF) Special Drawing Rights')),
    ('XOF', _('XOF - Communauté Financière Africaine (BCEAO) Franc')),
    ('XPF', _('XPF - Comptoirs Français du Pacifique (CFP) Franc')),
    ('YER', _('YER - Yemen Rial')),
    ('ZAR', _('ZAR - South Africa Rand')),
    ('ZMK', _('ZMK - Zambia Kwacha')),
    ('ZWD', _('ZWD - Zimbabwe Dollar')),
)

languages = []
languages_native = []
languages_english = []

if babel:
    locales = babel.localedata.list()
    locales.sort()
    for l_id in locales:
        l = babel.Locale(l_id)
        if l.english_name:
            languages_english.append((l_id, _(l.english_name)))
            if l.display_name:
                languages_native.append((l_id, l.display_name))
                if l.display_name == l.english_name:
                    label = '%s' % l.english_name
                else:
                    label = '%s (%s)' % (l.display_name, l.english_name)
                languages.append((l_id, label))


class Country(models.Model):
    """
    Country model
    =============

    Stores 2-letter ISO country code 2-letter continent code
    """

    code = models.CharField(_('country'), max_length=2, choices=countries,
                            unique=True)
    continent = models.CharField(_('continent'), max_length=2,
                                 choices=continents)

    def __str__(self):
        return self.get_code_display()

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')
