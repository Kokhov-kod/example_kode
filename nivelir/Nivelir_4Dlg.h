// Nivelir_4Dlg.h : header file
//
//{{AFX_INCLUDES()
#include "msflexgrid.h"
//}}AFX_INCLUDES

#if !defined(AFX_NIVELIR_4DLG_H__6ADFE272_6DC7_404E_B878_284F7999F7D0__INCLUDED_)
#define AFX_NIVELIR_4DLG_H__6ADFE272_6DC7_404E_B878_284F7999F7D0__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CNivelir_4Dlg dialog

class CNivelir_4Dlg : public CDialog
{
// Construction
public:
	CNivelir_4Dlg(CWnd* pParent = NULL);	// standard constructor

// Dialog Data
	//{{AFX_DATA(CNivelir_4Dlg)
	enum { IDD = IDD_NIVELIR_4_DIALOG };
	float	m_edit1;
	float	m_edit2;
	int		m_edit3;
	float	m_edit4;
	float	m_edit6;
	float	m_edit5;
	CMSFlexGrid	m_FG1;
	CMSFlexGrid	m_FG2;
	//}}AFX_DATA

	// ClassWizard generated virtual function overrides
	//{{AFX_VIRTUAL(CNivelir_4Dlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV support
	//}}AFX_VIRTUAL

// Implementation
protected:
	HICON m_hIcon;

	// Generated message map functions
	//{{AFX_MSG(CNivelir_4Dlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	virtual void OnOK();
	afx_msg void OnClickMsFlexgrid1();
	afx_msg void OnKeyPressMsFlexgrid1(short FAR* KeyAscii);
	afx_msg void OnButton1();
	afx_msg void OnButton2();
	DECLARE_EVENTSINK_MAP()
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ will insert additional declarations immediately before the previous line.

#endif // !defined(AFX_NIVELIR_4DLG_H__6ADFE272_6DC7_404E_B878_284F7999F7D0__INCLUDED_)
