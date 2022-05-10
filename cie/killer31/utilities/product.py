product = {
         'Killer_3.1' : {
                'check_activity' : {
                             'path' : '%ProgramData%\RivetNetworks\Killer\ActivityLog' ,
                             'files' : ['ActivityLog.db', 'AppDomainStatistics_ActivityLog.etl', 'IntelligenceEvents_ActivityLog.etl', 'UserInteraction_ActivityLog.etl']
                            },
##                'check_appdata': {
##                           # os.helper might be able to provide the path.
##                            'path' : '%USERPROFILE%\AppData\Local\Intel' ,
##                            'files' : ['user.config']
##                            },
                'check_appx' : {
##                                 #Maybe we can wildcard the name:
##                                 #C:/Program Files/WindowsApps/AppUp.IntelConnectivityPerformanceSuite_1.1021.1110.0_x64__121mr4mtzh4gw
                                'path': '%programfiles%\WindowsApps\RivetNetworks.KillerControlCenter_3.1*' ,
                                'files' : [
                                      'AppxBlockMap.xml', 'AppxManifest.xml', 'AppxSignature.p7x', 'KillerNetworkManagerlauncher.exe',
                                      'KillerNetworkManagerlauncherMinimized.exe', 'resources.pri',

                                      '\AppxMetadata\CodeIntegrity.cat',

                                      '\Assets\Square150x150Logo.scale-100.png', '\Assets\Square150x150Logo.scale-125.png', '\Assets\Square150x150Logo.scale-150.png',
                                      '\Assets\Square150x150Logo.scale-200.png', '\Assets\Square150x150Logo.scale-400.png', '\Assets\Square310x310Logo.scale-100.png',
                                      '\Assets\Square310x310Logo.scale-125.png', '\Assets\Square310x310Logo.scale-150.png', '\Assets\Square310x310Logo.scale-200.png',
                                      '\Assets\Square310x310Logo.scale-400.png', '\Assets\Square44x44Logo.scale-100.png', '\Assets\Square44x44Logo.scale-125.png',
                                      '\Assets\Square44x44Logo.scale-150.png', '\Assets\Square44x44Logo.scale-200.png', '\Assets\Square44x44Logo.scale-400.png',
                                      '\Assets\Square44x44Logo.targetsize-16.png', '\Assets\Square44x44Logo.targetsize-16_altform-unplated.png',
                                      '\Assets\Square44x44Logo.targetsize-24.png', '\Assets\Square44x44Logo.targetsize-24_altform-unplated.png',
                                      '\Assets\Square44x44Logo.targetsize-256.png', '\Assets\Square44x44Logo.targetsize-256_altform-unplated.png',
                                      '\Assets\Square44x44Logo.targetsize-32.png', '\Assets\Square44x44Logo.targetsize-32_altform-unplated.png',
                                      '\Assets\Square44x44Logo.targetsize-48.png', '\Assets\Square44x44Logo.targetsize-48_altform-unplated.png',
                                      '\Assets\Square71x71Logo.scale-100.png', '\Assets\Square71x71Logo.scale-125.png', '\Assets\Square71x71Logo.scale-150.png',
                                      '\Assets\Square71x71Logo.scale-200.png', '\Assets\Square71x71Logo.scale-400.png', '\Assets\StoreLogo.scale-100.png',
                                      '\Assets\StoreLogo.scale-125.png', '\Assets\StoreLogo.scale-150.png', '\Assets\StoreLogo.scale-200.png',
                                      '\Assets\StoreLogo.scale-400.png', '\Assets\Wide310x150Logo.scale-100.png', '\Assets\Wide310x150Logo.scale-125.png',
                                      '\Assets\Wide310x150Logo.scale-150.png', '\Assets\Wide310x150Logo.scale-200.png', '\Assets\Wide310x150Logo.scale-400.png',

                                      '\KillerControlCenter_v2\AnalyticsDataAcess.dll', '\KillerControlCenter_v2\DevExpress.BonusSkins.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.Charts.v20.2.Core.dll', '\KillerControlCenter_v2\DevExpress.Data.Desktop.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.Data.v20.2.dll', '\KillerControlCenter_v2\DevExpress.DataVisualization.v20.2.Core.dll',
                                      '\KillerControlCenter_v2\DevExpress.Images.v20.2.dll', '\KillerControlCenter_v2\DevExpress.Office.v20.2.Core.dll',
                                      '\KillerControlCenter_v2\DevExpress.Pdf.v20.2.Core.dll', '\KillerControlCenter_v2\DevExpress.Printing.v20.2.Core.dll',
                                      '\KillerControlCenter_v2\DevExpress.RichEdit.v20.2.Core.dll', '\KillerControlCenter_v2\DevExpress.RichEdit.v20.2.Export.dll',
                                      '\KillerControlCenter_v2\DevExpress.Sparkline.v20.2.Core.dll', '\KillerControlCenter_v2\DevExpress.Utils.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.Utils.v20.2.UI.dll', '\KillerControlCenter_v2\DevExpress.XtraBars.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraCharts.v20.2.dll', '\KillerControlCenter_v2\DevExpress.XtraCharts.v20.2.UI.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraCharts.v20.2.Wizard.dll', '\KillerControlCenter_v2\DevExpress.XtraEditors.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraGauges.v20.2.Core.dll', '\KillerControlCenter_v2\DevExpress.XtraGauges.v20.2.Win.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraGrid.v20.2.dll', '\KillerControlCenter_v2\DevExpress.XtraLayout.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraNavBar.v20.2.dll', '\KillerControlCenter_v2\DevExpress.XtraPrinting.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraRichEdit.v20.2.dll', '\KillerControlCenter_v2\DevExpress.XtraTreeList.v20.2.dll',
                                      '\KillerControlCenter_v2\DevExpress.XtraVerticalGrid.v20.2.dll', '\KillerControlCenter_v2\HtmlAgilityPack.dll',
                                      '\KillerControlCenter_v2\KAPSApi.dll', '\KillerControlCenter_v2\KillerIntelligenceCenter.exe',
                                      '\KillerControlCenter_v2\KillerNetworkManager_SmartAP.dll', '\KillerControlCenter_v2\KillerNetworkManager_WifiHotspot.dll',
                                      '\KillerControlCenter_v2\KillerNetworkServiceLib.dll', '\KillerControlCenter_v2\KillerNetworkServicePS.dll',
                                      '\KillerControlCenter_v2\Microsoft.Web.WebView2.Core.dll', '\KillerControlCenter_v2\Microsoft.Web.WebView2.WinForms.dll',
                                      '\KillerControlCenter_v2\Microsoft.Web.WebView2.Wpf.dll', '\KillerControlCenter_v2\ProximityLockApi.dll',
                                      '\KillerControlCenter_v2\RNC_Skin.dll', '\KillerControlCenter_v2\RNService.dll', '\KillerControlCenter_v2\RNTypes.dll',
                                      '\KillerControlCenter_v2\RNUserControls.dll', '\KillerControlCenter_v2\RNUtils.dll', '\KillerControlCenter_v2\RNUX.dll',
                                      '\KillerControlCenter_v2\RN_Skin.dll', '\KillerControlCenter_v2\runtime', '\KillerControlCenter_v2\SpeedtestCustom.exe',
                                      '\KillerControlCenter_v2\SQLite.Interop.dll', '\KillerControlCenter_v2\System.Data.SQLite.dll',
                                      '\KillerControlCenter_v2\WebView2Loader.dll', '\KillerControlCenter_v2\WifiCredentialPrompter.exe'
                                      ]
                               },
                'check_config' : {
                            'path': '%programdata%\RivetNetworks\Killer\ConfigurationFiles' ,
                            'files' : ['oem.xml', 'rn.stg', 'user.xml']
                            },
                'check_drivers' : {
                           'path':'%Systemroot%/System32/drivers/RivetNetworks/Killer',
                            'files':[
                                  'CustomizeInstallFirstRun.exe', 'KAPS.exe', 'KAPSService.exe', 'KAPSService.xml', 'keysink.exe', 'KfeCo10x64.sys', 'KillerAnalyticsService.exe',
                    'KillerEventLogMessages.dll', 'KillerLU.exe', 'KillerNetworkService', 'KNDBWM.exe', 'KNDBWMService.exe', 'KNDBWMService.xml', 'KSPS.exe', 'KSPSService.exe',
                    'KSPSService.xml', 'oem.xml', 'rn.stg', 'user.xml', 'xTendSoftAP.exe', 'xTendSoftAPService.exe', 'xTendUtility.exe', 'xTendUtilityService.exe', 'xTendUtilityService.xml'
                    ]
                             },
                'check_programfiles' : { None : []
                                 },
                'check_kernel_driver_file' : {
                                    'Win_10' : 'KfeCo10X64.sys',
                                    'Win_11' : 'KfeCo11X64.sys'
                                      },
                'confirm_status' :  {
                                    'services' : ['KNDBWM', 'Killer Analytics Service', 'Killer Network Service', 'KAPSService']
                                    # Think about Startup Type and any additional things to add here.
                                    },
                'install_driver' :  {
                                    'paths' : ['/UWD/Win64/Drivers/KillerNetworkExtension/', '/UWD/Win64/Drivers/KillerNetworkComponent/'],
                                    'files' : ['KillerNetworkExtension.inf', 'KillerNetworkComponent.inf']
                                    },
                'install_appx' :    {
                                   'paths' : ['/UWD/Win64/App/'],
                                   'files' : ['KillerControlCenter.appx']
                                   },
                'get_details' :     {
                                    'appx_name' : 'RivetNetworks.KillerControlCenter',
                                    'extension_file' : 'killernetworkextension.inf',
                                    'component_file' : 'killernetworkcomponent.inf',
                                    'driver_name' : 'Killer Networking Software'
                                    },
                'ui_details': {
                                'ui_title' : 'Killer Intelligence Center',
##                                'dialog_titles' : {'Advanced Settings':'SettingsWindow', 'Advanced Options':'Advanced Options'}
                            }
                     }
        }
