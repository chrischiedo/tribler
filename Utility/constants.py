# Various constants

#
# Constants used for keeping track of a torrent's status
#
STATUS_QUEUE      = 0
STATUS_STOP       = 200
STATUS_ACTIVE     = 100
STATUS_HASHCHECK  = 101
STATUS_PAUSE      = 102
STATUS_SUPERSEED  = 103
STATUS_FINISHED   = 300

#
# Constants for the column headings in the torrent list
#
COL_TITLE         = 4
COL_PROGRESS      = 5
COL_BTSTATUS      = 6
COL_PRIO          = 7
COL_ETA           = 8
COL_SIZE          = 9
COL_DLSPEED       = 10
COL_ULSPEED       = 11
COL_RATIO         = 12
COL_MESSAGE       = 13
COL_SEEDS         = 14
COL_PEERS         = 15
COL_COPIES        = 16
COL_PEERPROGRESS  = 17
COL_DLSIZE        = 18
COL_ULSIZE        = 19
COL_TOTALSPEED    = 20
COL_NAME          = 21
COL_DEST          = 22
COL_SEEDTIME      = 23
COL_CONNECTIONS   = 24
COL_SEEDOPTION    = 25
# only for tribler GUI:
COL_DLANDTOTALSIZE = 30


#
# Constants used for the column headings in the spew list
#
SPEW_UNCHOKE      = 0
SPEW_IP           = 1
SPEW_LR           = 2
SPEW_UP           = 3
SPEW_INTERESTED   = 4
SPEW_CHOKING      = 5
SPEW_DOWN         = 6
SPEW_INTERESTING  = 7
SPEW_CHOKED       = 8
SPEW_SNUBBED      = 9
SPEW_DLSIZE       = 10
SPEW_ULSIZE       = 11
SPEW_PEERPROGRESS = 12
SPEW_PEERSPEED    = 13
SPEW_PERMID       = 14

#
# Constants used for headings in the file info list
#
FILEINFO_FILENAME = 0
FILEINFO_SIZE     = 1
FILEINFO_PROGRESS = 2
FILEINFO_MD5      = 3
FILEINFO_CRC32    = 4
FILEINFO_SHA1     = 5
FILEINFO_ED2K     = 6

ACTION_SEPARATOR = -1 # Just to represent a separator within a menu/toolbar
ACTION_MOVEUP = 0
ACTION_MOVEDOWN = 1
ACTION_MOVETOP = 2
ACTION_MOVEBOTTOM = 3
ACTION_CLEARCOMPLETED = 4
ACTION_PAUSEALL = 5
ACTION_STOPALL = 6
ACTION_UNSTOPALL = 7
ACTION_WEBSERVICE = 8
ACTION_ADDTORRENT = 9
ACTION_ADDTORRENTNONDEFAULT = 10
ACTION_ADDTORRENTURL = 11
ACTION_RESUME = 12
#ACTION_RESEEDRESUME = 13
ACTION_PAUSE = 14
ACTION_STOP = 15
ACTION_QUEUE = 16
ACTION_REMOVE = 17
ACTION_REMOVEFILE = 18
ACTION_SCRAPE = 19
ACTION_DETAILS = 20
ACTION_SUPERSEED = 21
ACTION_HASHCHECK = 22
ACTION_CLEARMESSAGE = 23
ACTION_LOCALUPLOAD = 24
ACTION_OPENDEST = 25
ACTION_OPENFILEDEST = 26
ACTION_PREFERENCES = 27
ACTION_ABOUT = 28
ACTION_CHECKVERSION = 29
ACTION_MAKETORRENT = 30
ACTION_WEBPREFERENCES = 31
ACTION_EXTRACTFROMLIST = 32
ACTION_COPYFROMLIST = 33
ACTION_MANUALANNOUNCE = 34
ACTION_EXTERNALANNOUNCE = 35
ACTION_CHANGEDEST = 36
ACTION_CHANGEPRIO = 37
ACTION_EXPORTMENU = 38
ACTION_TORRENTACTIONMENU = 39
ACTION_FILEMENU = 40
ACTION_VERSIONMENU = 41
ACTION_TOOLSMENU = 42
ACTION_ADDTORRENTMENU = 43
ACTION_EXIT = 44
ACTION_BUDDIES = 45    # Tribler
ACTION_FILES = 46      # Tribler
ACTION_MYINFO = 47     # Tribler
SPINNER_NUMSIM = 1

#
# Constants used for recommended torrent list
#
TORRENT_TORRENTNAME = 0
TORRENT_CONTENTNAME = 1
TORRENT_RECOMMENDATION = 2
TORRENT_SOURCES = 3
TORRENT_NLEECHERS = 4
TORRENT_NSEEDERS = 5
TORRENT_INJECTED = 6
TORRENT_SIZE = 7
TORRENT_NFILES = 8
TORRENT_TRACKER = 9
TORRENT_CATEGORY = 10

#
# Constants used for my preference list
#
MYPREF_TORRENTNAME = 0
MYPREF_CONTENTNAME = 1
MYPREF_RANK = 2
MYPREF_SIZE = 3
MYPREF_LASTSEEN = 4

#
# Constants used for taste buddy list
#
BUDDY_FRIEND = 0
BUDDY_NAME = 1
BUDDY_IP = 2
BUDDY_SIM = 3
BUDDY_LASTSEEN = 4
BUDDY_NPREF = 5
BUDDY_NCONN = 6
BUDDY_NEXNG = 7


#
# Constants used for my download history list
#
HISTORY_TORRENTNAME = 0
HISTORY_CONTENTNAME = 1
HISTORY_RANK = 2
HISTORY_SIZE = 3
HISTORY_LASTSEEN =4

#
# Constants used for encountered peer list
#
PEER_FRIEND = 0
PEER_NAME = 1
PEER_IP = 2
PEER_SIMILARITY = 3
PEER_LASTSEEN = 4
PEER_PREFERENCES = 5
PEER_CONNECTED = 6
PEER_EXCHANGED = 7
