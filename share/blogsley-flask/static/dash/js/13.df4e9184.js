(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[13],{f62e:function(e,n,a){"use strict";a.r(n);var _=function(){var e=this,n=e.$createElement,a=e._self._c||n;return a("q-page",{attrs:{padding:""}},[e.$apollo.loading?a("div",[e._v("Loading..")]):a("div",{staticStyle:{width:"500px","max-width":"90vw"}},[a("q-list",{staticClass:"menu-list"},e._l(e.allPosts.edges,(function(n){return a("q-item",{key:n.id,attrs:{to:"/pages/"+n.node.id}},[a("q-item-section",{attrs:{avatar:""}},[a("q-icon",{attrs:{name:"mdi-file-document-outline",inverted:"",color:"grey-6"}})],1),a("q-item-section",[e._v("\n          "+e._s(n.node.title)+"\n        ")])],1)})),1)],1)])},s=[],i=a("a599"),p=a.n(i),o=a("1b62"),t=function(){var e=this,n=e.$createElement,a=e._self._c||n;return a("div",{staticClass:"fit"},[a("navbox-shell",[a("q-list",[a("q-item",{attrs:{to:"/pages/create",exact:""}},[a("q-item-section",{attrs:{avatar:""}},[a("q-icon",{attrs:{name:"note_add"}})],1),a("q-item-section",[a("q-item-label",[e._v("Add Page")])],1)],1)],1)],1)],1)},r=[],c=a("534b"),l=a("9c80"),d={name:"DefaultNavbox",mixins:[c["a"]],props:[],components:{NavboxShell:l["a"]},methods:{}},m=d,u=a("2be6"),g=Object(u["a"])(m,t,r,!1,null,null,null),b=g.exports,k=function(){var e=this,n=e.$createElement,a=e._self._c||n;return a("header-shell",[a("h1",[a("q-icon",{staticClass:"header-icon",attrs:{name:"mdi-book-open-page-variant"}}),e._v("\n    Pages\n  ")],1)])},v=[],h={name:"UsersHeader",mixins:[c["a"]],props:[],components:{},methods:{}},E=h,S=Object(u["a"])(E,k,v,!1,null,null,null),D=S.exports,f=a("1f9a"),O=a.n(f);function y(){var e=p()(["\nquery postQuery {\n  allPosts "," {\n    edges {\n      node {\n        id\n        title\n      }\n    }\n  }\n}\n"]);return y=function(){return e},e}var I=Object({NODE_ENV:"production",CLIENT:!0,SERVER:!1,DEV:!1,PROD:!0,MODE:"pwa",LESSOPEN:"| /usr/bin/lesspipe %s",npm_package_dependencies_vue_tippy:"^4.3.0",USER:"kurtis",npm_package_devDependencies_eslint_plugin_standard:"^4.0.0",npm_config_version_commit_hooks:"true",npm_config_user_agent:"yarn/1.22.4 npm/? node/v12.14.1 linux x64",npm_package_dependencies__quasar_extras:"^1.7.0",npm_config_bin_links:"true",SSH_AGENT_PID:"4850",XDG_SESSION_TYPE:"x11",npm_node_execpath:"/home/kurtis/.nvm/versions/node/v12.14.1/bin/node",npm_package_devDependencies_eslint_plugin_node:"^11.0.0",npm_package_dependencies_vue_apollo:"^3.0.2",npm_config_init_version:"1.0.0",SHLVL:"1",npm_package_resolutions__babel_parser:"7.7.5",npm_package_files_0:"dist",npm_package_publishConfig_access:"public",QT4_IM_MODULE:"ibus",HOME:"/home/kurtis",CHROME_DESKTOP:"code-url-handler.desktop",CONDA_SHLVL:"0",OLDPWD:"/home/kurtis/Dev/blogsley",npm_package_dependencies_apollo_link_error:"^1.1.10",npm_package_scripts_copy_dist:"yarn run copyfiles dist/* dist/**/* dist/**/**/* ../../",npm_package_files_1:"src",TERM_PROGRAM_VERSION:"1.44.2",DESKTOP_SESSION:"ubuntu",NVM_BIN:"/home/kurtis/.nvm/versions/node/v12.14.1/bin",GIO_LAUNCHED_DESKTOP_FILE:"/usr/share/applications/code.desktop",npm_package_engines_node:">= 10.18.1",npm_package_dependencies_vue_draggable_resizable:"^2.1.0",npm_package_dependencies_quasar:"^1.10.0",npm_config_init_license:"MIT",GNOME_SHELL_SESSION_MODE:"ubuntu",GTK_MODULES:"gail:atk-bridge",YARN_WRAP_OUTPUT:"false",npm_package_devDependencies_eslint_loader:"^3.0.3",npm_config_version_tag_prefix:"v",MANAGERPID:"4580",npm_package_dependencies_graphql_tag:"^2.10.1",DBUS_STARTER_BUS_TYPE:"session",DBUS_SESSION_BUS_ADDRESS:"unix:path=/run/user/1000/bus,guid=c44740871d92b85f8a2a23625eaca75b",npm_package_devDependencies_electron_devtools_installer:"^2.2.4",npm_package_dependencies_dotenv:"^8.2.0",npm_package_dependencies_copy_webpack_plugin:"^5.1.1",COLORTERM:"truecolor",_CE_M:"",GIO_LAUNCHED_DESKTOP_FILE_PID:"15220",npm_package_dependencies_apollo_cache_inmemory:"^1.6.5",npm_package_description:"Web Publishing Evolved.  A GraphQL CMS for the JAMstack!",NVM_DIR:"/home/kurtis/.nvm",npm_package_readmeFilename:"README.md",npm_package_dependencies_jwt_decode:"^2.2.0",MANDATORY_PATH:"/usr/share/gconf/ubuntu.mandatory.path",IM_CONFIG_PHASE:"1",GTK_IM_MODULE:"ibus",LOGNAME:"kurtis",npm_package_devDependencies_eslint_plugin_import:"^2.14.0",npm_package_dependencies_vue2_dropzone:"^3.6.0",JOURNAL_STREAM:"9:56455",_:"/home/kurtis/.yarn/bin/yarn",npm_package_devDependencies_node_sass:"^4.13.1",npm_package_devDependencies_eslint_config_standard:"^14.1.0",PUBLIC_PATH:"/dash/",XDG_SESSION_CLASS:"user",DEFAULTS_PATH:"/usr/share/gconf/ubuntu.default.path",npm_package_dependencies_apollo_link_http:"^1.5.14",npm_package_scripts_lint:"eslint --ext .js,.vue src",npm_package_productName:"Blogsley",npm_config_registry:"https://registry.yarnpkg.com",USERNAME:"kurtis",TERM:"xterm-256color",GNOME_DESKTOP_SESSION_ID:"this-is-deprecated",_CE_CONDA:"",npm_config_ignore_scripts:"",WINDOWPATH:"2",npm_package_dependencies_axios:"^0.19.1",npm_package_dependencies_apollo_link:"^1.2.11",npm_package_author_email:"kurtisfields@gmail.com",npm_package_cordovaId:"org.cordova.quasar.app",PATH:"/tmp/yarn--1588545185575-0.5720512696677471:/home/kurtis/Dev/blogsley/blogsley/blogsley/node_modules/.bin:/home/kurtis/.config/yarn/link/node_modules/.bin:/home/kurtis/Dev/blogsley/node_modules/.bin:/home/kurtis/.nvm/versions/node/v12.14.1/libexec/lib/node_modules/npm/bin/node-gyp-bin:/home/kurtis/.nvm/versions/node/v12.14.1/lib/node_modules/npm/bin/node-gyp-bin:/home/kurtis/.nvm/versions/node/v12.14.1/bin/node_modules/npm/bin/node-gyp-bin:/home/kurtis/.yarn/bin:/home/kurtis/.local/bin:/home/kurtis/.cargo/bin:/home/kurtis/.yarn/bin:/home/kurtis/.nvm/versions/node/v12.14.1/bin:/home/kurtis/.local/bin:/home/kurtis/anaconda3/condabin:/home/kurtis/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin",NODE:"/home/kurtis/.nvm/versions/node/v12.14.1/bin/node",SESSION_MANAGER:"local/jakyl:@/tmp/.ICE-unix/4963,unix/jakyl:/tmp/.ICE-unix/4963",INVOCATION_ID:"b5d702c15215483a8348f8b43f166777",npm_package_dependencies_js_beautify:"^1.10.3",npm_package_scripts_copy_netlify:"yarn run copyfiles _redirects ../../dist",npm_package_name:"@blogsley/blogsley",XDG_MENU_PREFIX:"gnome-",XDG_RUNTIME_DIR:"/run/user/1000",npm_package_devDependencies_devtron:"^1.4.0",npm_package_scripts_postdeploy:"yarn run copy:dist && yarn run copy:netlify",DISPLAY:":1",LANG:"en_US.UTF-8",XDG_CURRENT_DESKTOP:"Unity",npm_package_devDependencies_strip_ansi:"6.0.0",npm_package_devDependencies_eslint:"^6.8.0",npm_package_devDependencies_electron_debug:"^3.0.0",npm_package_dependencies_dexie_observable:"^1.0.0-beta.5",npm_package_dependencies_apollo_boost:"^0.4.7",npm_package_dependencies__blocksley_quasar_app_extension_blocksley:"^0.1.30-alpha.0",XMODIFIERS:"@im=ibus",XDG_SESSION_DESKTOP:"ubuntu",XAUTHORITY:"/run/user/1000/gdm/Xauthority",LS_COLORS:"rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:",TERM_PROGRAM:"vscode",npm_lifecycle_script:"quasar build -m pwa",npm_package_browserslist_0:"last 1 version, not dead, ie >= 11",SSH_AUTH_SOCK:"/run/user/1000/keyring/ssh",CONDA_PYTHON_EXE:"/home/kurtis/anaconda3/bin/python",npm_package_devDependencies__quasar_app:"^1.8.3",npm_package_dependencies_vue_lazyload:"^1.2.6",npm_package_scripts_test:'echo "No test specified" && exit 0',npm_config_version_git_message:"v%s",SHELL:"/bin/bash",npm_lifecycle_event:"build",npm_package_dependencies_nanoid:"^2.1.10",npm_package_version:"0.1.30-alpha.0",NO_AT_BRIDGE:"1",GDMSESSION:"ubuntu",npm_config_argv:'{"remain":[],"cooked":["run","build"],"original":["build"]}',npm_package_engines_yarn:">= 1.21.1",npm_package_dependencies_graphql:"^14.3.1",npm_package_scripts_build:"quasar build -m pwa",LESSCLOSE:"/usr/bin/lesspipe %s %s",npm_package_devDependencies_sass_loader:"^8.0.2",npm_package_dependencies_apollo_link_context:"^1.0.19",npm_config_version_git_tag:"true",npm_config_version_git_sign:"",GPG_AGENT_INFO:"/run/user/1000/gnupg/S.gpg-agent:0:1",npm_package_devDependencies_copyfiles:"^2.2.0",npm_package_license:"MIT",npm_config_strict_ssl:"true",QT_IM_MODULE:"ibus",npm_package_dependencies_subscriptions_transport_ws:"^0.9.16",npm_package_dependencies_apollo_utilities:"^1.3.3",PWD:"/home/kurtis/Dev/blogsley/blogsley/blogsley",npm_execpath:"/home/kurtis/.config/yarn/global/node_modules/yarn/bin/yarn.js",XDG_CONFIG_DIRS:"/etc/xdg/xdg-ubuntu:/etc/xdg",CONDA_EXE:"/home/kurtis/anaconda3/bin/conda",CLUTTER_IM_MODULE:"ibus",NVM_CD_FLAGS:"",DBUS_STARTER_ADDRESS:"unix:path=/run/user/1000/bus,guid=c44740871d92b85f8a2a23625eaca75b",XDG_DATA_DIRS:"/home/kurtis/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/home/kurtis/.local/share/flatpak/exports/share:/var/lib/flatpak/exports/share:/usr/share/ubuntu:/home/kurtis/.local/share/flatpak/exports/share/:/var/lib/flatpak/exports/share/:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop",npm_package_engines_npm:">= 6.13.4",npm_package_devDependencies_electron:"^7.0.0",npm_package_dependencies_apollo_client:"^2.6.8",npm_package_author_name:"Kurtis Fields",npm_package_devDependencies_eslint_plugin_vue:"^6.1.2",npm_config_save_prefix:"^",npm_config_ignore_optional:"",npm_package_devDependencies_babel_eslint:"^10.0.1",npm_package_scripts_deploy:"quasar build -m pwa",npm_package_devDependencies_eslint_plugin_promise:"^4.0.1",npm_package_dependencies_apollo_link_ws:"^1.0.19",INIT_CWD:"/home/kurtis/Dev/blogsley/blogsley/blogsley",npm_package_dependencies_dexie:"^2.0.4",SERVER_URL:"http://127.0.0.1:5000",AUTH_USER:"admin",AUTH_PWD:"admin",GRAPHQL_URL:"http://127.0.0.1:5000/graphql/",SUBSCRIPTIONS_URL:"ws://127.0.0.1:5000/graphql/",VUE_ROUTER_MODE:"history",VUE_ROUTER_BASE:"/dash/",APP_URL:"undefined",SERVICE_WORKER_FILE:"/dash/service-worker.js"}).STANDALONE?"@client":"",R=O()(y(),I),N={name:"Posts",mixins:[o["b"],o["a"]],data:function(){return{title:"Pages",authorId:this.$route.params.authorId}},apollo:{allPosts:{query:R,variables:function(){return{authorId:this.authorId}}}},methods:{onSwitch:function(){this.setView(this),this.setNavbox(b),this.setHeader(D)}}},x=N,T=Object(u["a"])(x,_,s,!1,null,null,null);n["default"]=T.exports}}]);